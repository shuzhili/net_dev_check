#!/usr/bin/python3
#-*- coding:utf-8 -*-
import pexpect
import threading
import time
import datetime
import sys
import os
import re
import stat
#741_cisco_2960管理交换机的设备配置备份脚本
now_time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
file_name_date = time.strftime('%Y%m%d')#定义一个日期，以这个日期去命名文件夹
#os.mkdir("/root/Backup/MGMT-741/{}".format(file_name_date))

os.mkdir("/root/beifen/{}".format(file_name_date))#年月日
os.mkdir("/root/beifen/{}/KFCS".format(file_name_date))#年月日

#os.chmod("/var/ftp/{}/741-cisco-mgmt".format(file_name_date),stat.S_IRWXO)


def n_time():
    return '当前时间是:{}'.format(now_time)
def beifen_switch(switch_ip):
    try:
        child = pexpect.spawn('telnet {}'.format(switch_ip),timeout=180,maxread=90000000)
        fout = open('/root/beifen/{}/KFCS/backup_{}_log.txt'.format(file_name_date,switch_ip), 'ab')
        #以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
        #以日期和设备IP去命令备份的文件。
        child.logfile = fout
        login = child.expect(['.*login.*', '.*Username.*', pexpect.EOF, pexpect.TIMEOUT], timeout=30)
        if login == 0 or login == 1:
            child.sendline('test-user')
            child.expect('.*word:')
            child.sendline('test-passwd')
            child.expect('.*>')
            print ("login {} success!".format(switch_ip),n_time())
        else:
            #child.close(force=True)
            print ("login {} failed!!".format(switch_ip))
       #child.expect('.*#')
        child.sendline('sy ')
        child.expect('.*]',timeout=180)
        child.sendline('line vty 0 4')
        child.expect('.*]',timeout=180)
        child.sendline('screen-length 0')
        child.expect('.*]',timeout=180)
        child.sendline('quit')
        child.expect('.*]',timeout=180)
        child.sendline('dis cu ')
        child.expect('.*]',timeout=180)
        child.sendline('line vty 0 4')
        child.expect('.*]',timeout=180)
        child.sendline('undo screen-length')
        child.expect('.*]',timeout=180)
        child.sendline('quit')
        #child.sendline('copy runn start')
        child.expect('.*]',timeout=180)
        child.sendline('quit')

        print ("save sucess!{}".format(switch_ip),n_time())
    except:
        return -1
    return 0

IP_LIST = open('/root/PY_BeiFen_IP-list/kfcs-beifen-ip-list.txt', 'r')
for ipaddr in IP_LIST:
    switch_ip1 = ipaddr.split('.')[0]
    switch_ip2 = ipaddr.split('.')[1]
    switch_ip3 = ipaddr.split('.')[2]
    switch_ip4 = ipaddr.split('.')[3]
    switch_ip5 = switch_ip1 + '.' + switch_ip2 + '.' + switch_ip3 + '.' + switch_ip4

    switch_ip6 = switch_ip5.strip()#去除IP的多余字符


    beifen_switch(switch_ip6)

print("备份完成，x个设备，")
#filenu = os.system('ls -al {}|grep '^-'|wc -l'.format(file_name_date))
#print("备份的设备有:",fulenu)