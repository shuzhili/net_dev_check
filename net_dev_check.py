# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv
import wx.lib.calendar
import autocheck_net
# from dateTime import countone

from deviceType import Device


###########################################################################
## Class MyFrame2
#################################import_config##########################################

class MyFrame2(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"昆仑银行网络自动运维工具", pos=wx.DefaultPosition,
                          size=wx.Size(400, 400), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        # 设置图标
        self.icon1 = wx.Icon(name="logo2.ico", type=wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon1)
        # 设置图标

        # 底部状态栏
        bottomStatusBar = self.CreateStatusBar()
        self.SetStatusBar(bottomStatusBar)
        self.SetStatusText(u"总行网络团队提供")
        # 底部状态栏

        frame_bSizer = wx.BoxSizer(wx.VERTICAL)

        dev_bSizer = wx.BoxSizer(wx.HORIZONTAL)

        # 设备选择
        dev_select_bSizer = wx.BoxSizer(wx.VERTICAL)

        self.h3c_radioBtn = wx.RadioButton(self, wx.ID_ANY, u"h3c", wx.DefaultPosition, wx.DefaultSize, 0)
        dev_select_bSizer.Add(self.h3c_radioBtn, 1, wx.ALL, 5)

        self.cisco_radioBtn = wx.RadioButton(self, wx.ID_ANY, u"cisco", wx.DefaultPosition, wx.DefaultSize, 0)
        dev_select_bSizer.Add(self.cisco_radioBtn, 1, wx.ALL, 5)

        self.ruijie_radioBtn = wx.RadioButton(self, wx.ID_ANY, u"锐捷", wx.DefaultPosition, wx.DefaultSize, 0)
        dev_select_bSizer.Add(self.ruijie_radioBtn, 1, wx.ALL, 5)

        self.hw_radioBtn = wx.RadioButton(self, wx.ID_ANY, u"华为", wx.DefaultPosition, wx.DefaultSize, 0)
        dev_select_bSizer.Add(self.hw_radioBtn, 1, wx.ALL, 5)
        # 设备选择

        dev_bSizer.Add(dev_select_bSizer, 0, 1, 5)

        # ip 用户名 密码展示
        self.ip_name_pwd_txt = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, pos=(80, 20), size=(250, 120),
                                           style=wx.TE_MULTILINE | wx.BORDER_SIMPLE)

        self.ip_name_pwd_txt.Hide()

        dev_bSizer.Add(self.ip_name_pwd_txt, 1, wx.EXPAND, 5)
        # ip 用户名 密码展示

        frame_bSizer.Add(dev_bSizer, 1, wx.EXPAND, 5)

        bSizer10 = wx.BoxSizer(wx.VERTICAL)

        # //////////////////////设备IP地址 添加 清空
        ip_bSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, u"设备IP地址：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        ip_bSizer.Add(self.m_staticText2, 0, wx.ALL, 5)

        self.input_ip_tv = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        ip_bSizer.Add(self.input_ip_tv, 1, wx.ALL, 5)

        self.import_ip_bt = wx.Button(self, wx.ID_ANY, u"添加", wx.DefaultPosition, wx.DefaultSize, 0)
        ip_bSizer.Add(self.import_ip_bt, 0, wx.ALL, 5)

        self.clear_ip_path_bt = wx.Button(self, wx.ID_ANY, u"清空", wx.DefaultPosition, wx.DefaultSize, 0)
        ip_bSizer.Add(self.clear_ip_path_bt, 0, wx.ALL, 5)

        bSizer10.Add(ip_bSizer, 0, wx.EXPAND, 5)
        # //////////////////////设备IP地址 添加 清空

        # //////////////////////telnet ssh
        tel_ssh_bSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.telnet_bt = wx.RadioButton(self, wx.ID_ANY, u"telnet", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP)
        tel_ssh_bSizer.Add(self.telnet_bt, 1, wx.ALL, 5)

        self.ssh_bt = wx.RadioButton(self, wx.ID_ANY, u"ssh", wx.DefaultPosition, wx.DefaultSize, 0)
        tel_ssh_bSizer.Add(self.ssh_bt, 1, wx.ALL, 5)

        bSizer10.Add(tel_ssh_bSizer, 0, wx.EXPAND, 5)
        # //////////////////////telnet ssh

        # 日期选择
        # data_select_bSizer = wx.BoxSizer(wx.HORIZONTAL)
        #
        # self.edtDateb = wx.adv.DatePickerCtrl(self, id=-1, size=(90, 40), pos=(90, 30),
        #                                       style=wx.adv.DP_DROPDOWN | wx.adv.DP_SHOWCENTURY)
        # self.Bind(wx.adv.EVT_DATE_CHANGED, self.OnCalSelChangedb, self.edtDateb)
        #
        # font = wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.BOLD, True)
        # self.yearInput1 = wx.TextCtrl(self, -1, u'', pos=(190, 40), size=(60, -1))
        # self.yearInput1.SetForegroundColour('gray')
        # self.yearInput1.SetFont(font)
        #
        # data_select_bSizer.Add(self.edtDateb, 1, wx.ALL, 5)
        # data_select_bSizer.Add(self.yearInput1, 1, wx.ALL, 5)
        # bSizer10.Add(data_select_bSizer, 0, wx.EXPAND, 5)
        # 日期选择

        # 时间选择
        # time_select_bSizer = wx.BoxSizer(wx.HORIZONTAL)
        #
        # self.edtTimeb = wx.adv.TimePickerCtrl(self, id=-1, size=(90, 40), pos=(90, 30), style=wx.adv.DP_DEFAULT)
        # self.Bind(wx.adv.EVT_TIME_CHANGED, self.OnTimeSelChangedb, self.edtTimeb)
        #
        # font = wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.BOLD, True)
        # self.timeInput = wx.TextCtrl(self, -1, u'', pos=(190, 40), size=(60, -1))
        # self.timeInput.SetForegroundColour('gray')
        # self.timeInput.SetFont(font)
        #
        # time_select_bSizer.Add(self.edtTimeb, 1, wx.ALL, 5)
        # time_select_bSizer.Add(self.timeInput, 1, wx.ALL, 5)
        # bSizer10.Add(time_select_bSizer, 0, wx.EXPAND, 5)
        # 时间选择

        # //////////////////////开始备份定时任务
        begin_time_bSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.begin_backup_bt = wx.Button(self, wx.ID_ANY, u"开始备份", wx.DefaultPosition, wx.DefaultSize, 0)
        begin_time_bSizer.Add(self.begin_backup_bt, 1, wx.ALL, 5)

        self.time_bt = wx.Button(self, wx.ID_ANY, u"定时任务", wx.DefaultPosition, wx.DefaultSize, 0)
        begin_time_bSizer.Add(self.time_bt, 1, wx.ALL, 5)
        # //////////////////////开始备份定时任务

        bSizer10.Add(begin_time_bSizer, 1, wx.EXPAND, 5)

        frame_bSizer.Add(bSizer10, 1, wx.EXPAND, 5)

        self.SetSizer(frame_bSizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.h3c_radioBtn.Bind(wx.EVT_RADIOBUTTON, self.h3c_click)
        self.cisco_radioBtn.Bind(wx.EVT_RADIOBUTTON, self.cisco_click)
        self.ruijie_radioBtn.Bind(wx.EVT_RADIOBUTTON, self.ruijie_click)
        self.hw_radioBtn.Bind(wx.EVT_RADIOBUTTON, self.hw_click)
        self.import_ip_bt.Bind(wx.EVT_BUTTON, self.import_ip_click)
        self.clear_ip_path_bt.Bind(wx.EVT_BUTTON, self.clear_ip_path_click)
        self.telnet_bt.Bind(wx.EVT_RADIOBUTTON, self.telnet_click)
        self.ssh_bt.Bind(wx.EVT_RADIOBUTTON, self.ssh_click)
        self.begin_backup_bt.Bind(wx.EVT_BUTTON, self.start_backup_click)
        self.time_bt.Bind(wx.EVT_BUTTON, self.time_task_click)

    # 设置标志位
    isSSH = 0
    isTelnet = 0
    dev_Type = 1
    ipCfgPath = ""

    # 窗口销毁监听
    def __del__(self):
        print("dellll")
        pass

    # Virtual event handlers, overide them in your derived class
    def h3c_click(self, event):
        dev_Type = Device.H3C

    def cisco_click(self, event):
        dev_Type = Device.CISCO

    def ruijie_click(self, event):
        dev_Type = Device.RUIJIE

    def hw_click(self, event):
        dev_Type = Device.HW

    def import_ip_click(self, event):
        dlg = wx.FileDialog(self, u'选择要打开的txt文件', style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            self.input_ip_tv.SetValue(dlg.GetPath())
            ipCfgPath = dlg.GetPath()
            self.read_dev_config(ipCfgPath)
            dlg.Destroy()

    def clear_ip_path_click(self, event):
        # event.Skip()
        self.input_ip_tv.Clear()
        self.ip_name_pwd_txt.Clear()
        self.ip_name_pwd_txt.Hide()

    def telnet_click(self, event):
        self.isTelnet = 1

    def ssh_click(self, event):
        self.isSSH = 1

    def start_backup_click(self, event):
        autocheck_net.chech_dev(self.input_ip_tv.GetValue(), self.isSSH, self.isTelnet, self.dev_Type)

    def time_task_click(self, event):
        print("start timestask")

    def read_dev_config(self, path):
        f = open(path, "rb")
        lines = f.readlines()
        print(type(lines))
        for line in lines:
            self.ip_name_pwd_txt.AppendText(line)
        self.ip_name_pwd_txt.Show()
        f.close()

    def OnCalSelChangedb(self, event):
        cal = event.GetEventObject()
        datestr = cal.GetValue()
        beginyear = datestr.year
        beginmonth = str(int(datestr.month) + 1)
        beginday = datestr.day

        self.yearInput1.Clear()
        dataStr = str(beginyear) + "-" + str(beginmonth) + "-" + str(beginday)
        self.yearInput1.WriteText(dataStr)

    def OnTimeSelChangedb(self, event):
        cal = event.GetEventObject()
        timestr = cal.GetValue()
        self.timeInput.Clear()
        self.timeInput.WriteText(str(timestr))


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame2(None)
    frame.Show()
    app.MainLoop()
