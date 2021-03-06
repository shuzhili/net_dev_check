# -*-coding:utf-8-*-
import wx
import paramiko
import telnetlib
import socket
import time
import re
import fileinput
import os
import zipfile
import smtplib
import sys
import importlib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from deviceType import Device

from net_dev_check import Current_cwd

# import pdb

# --------------------------------------------------------

print(Current_cwd)
LogDir = Current_cwd + r'\log'
LogDirMailToday = LogDir + '\\' + time.strftime('%Y%m%d')  # 以日期创建目录
cmdfile_CISCO = Current_cwd + r'\etc\\CMD_Cisco.ini'
cmdfile_HW = Current_cwd + r'\etc\\CMD_HW.ini'
cmdfile_RUIJIE = Current_cwd + r'\etc\\CMD_Ruijie.ini'

SMTP_Sever = 'smtp.139.com'
Mail_List_File = Current_cwd + r'\etc\\Mail_list.ini'

ZipFileDir = LogDirMailToday
ZIPFILE = u'Network check' + os.path.basename(LogDirMailToday) + '.zip'

os.chdir(Current_cwd)

ip_cfg_path = ""
m_dev_type = Device.H3C


def OnCloseMe():
    dlg = wx.MessageDialog(None, u"完成", u"标题信息", wx.YES_NO | wx.ICON_QUESTION)
    if dlg.ShowModal() == wx.ID_YES:
        dlg.Destroy()


# ---------------------------------------------------------

def Read_IP_UserName_Pwd(path):
    f = open(path)
    data = []
    for lines in f.readlines():
        if lines.strip() == '':
            continue
        print('---------lsz-----lines------'+str(lines))
        (ip, name, pwd) = str(lines).split(" ")
        print('---------lsz-----(ip, name, pwd)------' + str((ip, name, pwd)))
        data.append((ip, name, pwd))
    f.close()
    return data


'''
Port_check
端口检测：
*.检测22和23端口，确定ssh/telnet登陆方式
*.端口都开放，根据测试结果选择登陆方式
*.将22，23端口检测失败的设备标记为failed
'''


def Port_check(Host, UserName, PassWord):
    failed_count_to = 0
    sc_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sc_tcp.settimeout(2)
    port_check_ssh = sc_tcp.connect_ex((Host, 22))
    sc_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sc_tcp.settimeout(2)
    port_check_telnet = sc_tcp.connect_ex((Host, 23))
    if port_check_ssh == 0 and port_check_telnet == 0:
        try:
            trans = paramiko.Transport((Host, 22))
            trans.start_client()
            trans.auth_password(username=UserName, password=PassWord)
        except Exception as Error_Message:
            Port = 23
        else:
            Port = 22
    elif port_check_telnet == 0 and port_check_ssh != 0:
        Port = 23
    elif port_check_ssh == 0 and port_check_telnet != 0:
        Port = 22
    else:
        os.chdir(LogDirMailToday)
        Error_Message = "Time Out"
        Log_Error_File = Host.strip() + '_failed.txt'
        print(Log_Error_File)
        log = open(Log_Error_File, 'a+')
        print("Port_check")
        Error_Log = 'ERROR:' + Host.strip() + ',' + str(Error_Message)
        log.write(Error_Log)
        log.close()
        Port = 'Null'
    # print Host,Port
    return (Port)


'''
AutoCheck_ssh()
使用ssh登陆方式巡检设备
*.账号登陆失败的设备标记为failed
'''


def AutoCheck_ssh(Host, UserName, PassWord, DeviceName):
    # paramiko.util.log_to_file('paramiko.log')
    content = ""
    success_count_ssh = 0
    failed_count_ssh = 0
    trans = paramiko.Transport((Host, 22))
    try:
        trans.start_client()
        trans.auth_password(username=UserName, password=PassWord)
    except Exception as Error_Message:
        os.chdir(LogDirMailToday)
        Log_Error_File = Host.strip() + '_failed.txt'
        log = open(Log_Error_File, 'a+')
        Error_Log = 'ERROR:' + Host.strip() + ',' + str(Error_Message) + '\r\n'
        log.write(Error_Log)
        log.close()
        failed_count_ssh = + 1
        trans.close()
    else:
        channel = trans.open_session()
        channel.get_pty()
        channel.invoke_shell()
        content = []
        # channel.sendall('su' + '\n')
        time.sleep(0.5)
        # channel.sendall(SuperPass + '\n')
        global cmdfile
        if DeviceName.find('3750') != -1:
            cmdfile = open(cmdfile_CISCO)
        else:
            cmdfile = open(cmdfile_HW)
        for cmd in cmdfile:
            # print cmd
            channel.sendall(cmd)
            time.sleep(0.5)
            content.append(channel.recv(9999))
        os.chdir(LogDirMailToday)
        LogFile = DeviceName + '.txt'
        log = open(LogFile, 'a+')
        for log_info in content:
            log.write(log_info)
        success_count_ssh = + 1
        channel.close()
        trans.close()
        cmdfile.close()
    return success_count_ssh, failed_count_ssh


'''
AutoCheck_telnet()
使用telnet登陆方式巡检设备
'''


def AutoCheck_telnet(Host, UserName, PassWord, DeviceName,IP_DIR):
    content = ""
    success_count_telnet = 0
    failed_count_telnet = 0
    global tn
    try:
        print('telnet start'+Host)
        tn = telnetlib.Telnet(bytes(str(Host), encoding="utf-8"), port=23)
        DeviceType = tn.expect([], timeout=1)[2].decode().strip()

        tn.set_debuglevel(2)
        tn.read_until(b"Username:", 1)
        tn.write(UserName.encode() + b"\n")
        tn.read_until(b"Password:", 1)
        tn.write(PassWord.encode() + b"\n")
        tn.write(5 * b'\n')

        print('=======deviceType========' + DeviceType)
        # pdb.set_trace()
        global cmdfile
        if DeviceName == Device.H3C or DeviceName == Device.HW:  # 华为或者华三设备
            cmdfile = open(cmdfile_HW)  # 命令列表
            tn.write('super'.encode() + b'\n')
        elif DeviceName == Device.CISCO:  # 思科设备
            cmdfile = open(cmdfile_CISCO)  # 命令列表
            tn.write('enable\n'.encode())
            time.sleep(1)
        elif DeviceName == Device.RUIJIE:
            cmdfile = open(cmdfile_RUIJIE)
            tn.write('enable'.encode() + b'\n')
        else:
            cmdfile = open(cmdfile_HW)
            tn.write('enable'.encode() + b'\n')
        print('telnet write data')
        for cmd in cmdfile:  # 输入列表的命令
            print('-----------lsz------------' + cmd.strip())
            tn.write(cmd.strip().encode())
            # 这里要等待一段时间
            time.sleep(2)
            tn.write(2 * b'\n')
            telreply = tn.expect([], timeout=10)[2].decode().strip()  # 输出日志
            print('-----lsz telreply------------' + str(telreply))
            content = str(content) + str(telreply)
        print('telnet write data finish')
        cmdfile.close()
        success_count_telnet = + 1
    except Exception as Error_Message:
        print('telnet exception ')
        print(IP_DIR)
        os.chdir(IP_DIR)
        Log_Error_File = Host.strip() + '_failed.txt'
        log = open(Log_Error_File, 'a+')
        Error_Log = 'ERROR:' + Host.strip() + ',' + str(Error_Message) + '\r\n'
        log.write(Error_Log)
        log.close()
        failed_count_telnet = + 1
    # finally:
    #     tn.close()
    #     del tn
    print(IP_DIR)
    os.chdir(IP_DIR)
    LogFile = str(DeviceName) + '.txt'
    log = open(LogFile, 'a+')  # 写入日志
    log.write(content)
    log.close()

    return success_count_telnet, failed_count_telnet


'''
Zip_File()
压缩日志函数
'''


def Zip_File():
    os.chdir(LogDir)
    LogZip = zipfile.ZipFile(ZIPFILE, 'w', zipfile.ZIP_DEFLATED)  # 压缩日志

    for filenames in os.walk(ZipFileDir):
        for filename in filenames[-1]:
            print(filename)
            LogZip.write(os.path.join(os.path.basename(LogDirMailToday) + '\\' + filename))
            os.remove(LogDirMailToday + '\\' + filename)  # 压缩完成后删除文件，以便后续删除原始目录
    LogZip.close()
    os.removedirs(LogDirMailToday)  # 压缩成功后，删除原始目录
    return ZIPFILE


'''
Send_Mail()
发送邮件函数
'''


def Send_Mail(success_count, failed_count, Mail_User, Mail_Pwd):
    Mail_List = open(Mail_List_File)  # 邮件地址列表
    Mail_To = []
    for list in Mail_List:  # 读取邮件列表文件
        Mail_To.extend(list.strip().split(','))
    Mail_List.close()
    msg = MIMEMultipart()
    importlib.reload(sys)
    Subject = '网络设备巡检-' + os.path.basename(LogDirMailToday)
    Content = '巡检成功: ' + str(success_count) + ' 巡检失败: ' + str(failed_count)
    Content = Content + '<br>' + '<br>' + "-----------" + '<br>' + "这是一份自动邮件，请不要回复！！"
    msg["Subject"] = Subject  # 邮件标题
    msg["From"] = Mail_User
    msg["To"] = ",".join(Mail_To)
    msgContent = MIMEText(Content, 'html', 'utf-8')  # 邮件内容
    msgContent["Accept-Language"] = "zh-CN"
    msgContent["Accept-Charset"] = "ISO-8859-1,utf-8"
    msg.attach(msgContent)
    attachment = MIMEApplication(open(ZIPFILE, 'rb').read())
    attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(ZIPFILE))
    msg.attach(attachment)
    s = smtplib.SMTP_SSL(SMTP_Sever, '465')
    s.ehlo()
    s.login(Mail_User, Mail_Pwd)
    s.sendmail(Mail_User, Mail_To, msg.as_string())  # 发送邮件
    s.close()


def chech_dev(path, isSSh, isTelnet, dev_type):
    ip_cfg_path = path
    m_dev_type = dev_type

    success_count = 0
    failed_count = 0

    data = Read_IP_UserName_Pwd(ip_cfg_path)

    if not os.path.exists(LogDirMailToday):
        os.makedirs(LogDirMailToday)

    for ip_name_pwd in data:
        success_count_ssh = 0
        success_count_telnet = 0
        failed_count_ssh = 0
        failed_count_telnet = 0
        failed_count_to = 0

        ip = ip_name_pwd[0]
        name = ip_name_pwd[1]
        pwd = ip_name_pwd[2]
        IP_DIR=LogDirMailToday+'\\'+ip
        print(IP_DIR)
        if not os.path.exists(IP_DIR):
            os.makedirs(IP_DIR)

        # (Port) = Port_check(ip, name, pwd)

        if isSSh:
            (success_count_ssh, failed_count_ssh) = AutoCheck_ssh(ip, name, pwd, m_dev_type)
        elif isTelnet:
            (success_count_telnet, failed_count_telnet) = AutoCheck_telnet(ip, name, pwd, m_dev_type, IP_DIR)
        else:
            failed_count_to = + 1
        success_count = success_count + success_count_ssh + success_count_telnet
        failed_count = failed_count + failed_count_ssh + failed_count_telnet + failed_count_to
    OnCloseMe()
    # Zip_File()
    print("success:%s" % success_count)
    print("fail:%s" % failed_count)
    Mail_User = "lishuzhi@wondertek.com.cn"
    Mail_Pwd = "123456lishuzhi"
    # Send_Mail(success_count, failed_count, Mail_User, Mail_Pwd)
# --------------------------------------------------------------------------
