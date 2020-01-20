# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import autocheck_net
from deviceType import Device


###########################################################################
## Class MyFrame2
#################################import_config##########################################

class MyFrame2(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"昆仑银行网络自动运维工具", pos=wx.DefaultPosition,
                          size=wx.Size(400, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.icon1 = wx.Icon(name="logo.ico", type=wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon1)

        bottomStatusBar = self.CreateStatusBar()
        self.SetStatusBar(bottomStatusBar)
        self.SetStatusText(u"总行网络团队提供")

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        bSizer3 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        self.h3c_radioBtn = wx.RadioButton(self, wx.ID_ANY, u"h3c", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.h3c_radioBtn, 1, wx.ALL, 5)

        self.cisco_radioBtn = wx.RadioButton(self, wx.ID_ANY, u"cisco", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.cisco_radioBtn, 1, wx.ALL, 5)

        self.ruijie_radioBtn = wx.RadioButton(self, wx.ID_ANY, u"锐捷", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.ruijie_radioBtn, 1, wx.ALL, 5)

        self.hw_radioBtn = wx.RadioButton(self, wx.ID_ANY, u"华为", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.hw_radioBtn, 1, wx.ALL, 5)

        bSizer3.Add(bSizer4, 0, 1, 5)

        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        self.import_config = wx.Button(self, wx.ID_ANY, u"批量导入", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer9.Add(self.import_config, 1, wx.ALL, 5)

        self.clear = wx.Button(self, wx.ID_ANY, u"清空", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer9.Add(self.clear, 1, wx.ALL, 5)

        bSizer3.Add(bSizer9, 0, 1, 5)

        self.config_content = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, 100),
                                          style=wx.TE_MULTILINE)

        bSizer3.Add(self.config_content, 1, wx.EXPAND, 5)

        bSizer1.Add(bSizer3, 1, wx.EXPAND, 5)

        bSizer10 = wx.BoxSizer(wx.VERTICAL)

        bSizer11 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, u"设备IP地址：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        bSizer11.Add(self.m_staticText2, 0, wx.ALL, 5)

        self.input_ip_tv = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer11.Add(self.input_ip_tv, 1, wx.ALL, 5)

        self.import_ip_bt = wx.Button(self, wx.ID_ANY, u"添加", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer11.Add(self.import_ip_bt, 0, wx.ALL, 5)

        self.clear_ip_path_bt = wx.Button(self, wx.ID_ANY, u"清空", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer11.Add(self.clear_ip_path_bt, 0, wx.ALL, 5)

        bSizer10.Add(bSizer11, 0, wx.EXPAND, 5)

        bSizer12 = wx.BoxSizer(wx.HORIZONTAL)

        self.telnet_bt = wx.RadioButton(self, wx.ID_ANY, u"telnet", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP)
        bSizer12.Add(self.telnet_bt, 1, wx.ALL, 5)

        self.ssh_bt = wx.RadioButton(self, wx.ID_ANY, u"ssh", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer12.Add(self.ssh_bt, 1, wx.ALL, 5)

        bSizer10.Add(bSizer12, 0, wx.EXPAND, 5)

        bSizer13 = wx.BoxSizer(wx.HORIZONTAL)

        self.begin_backup_bt = wx.Button(self, wx.ID_ANY, u"开始备份", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer13.Add(self.begin_backup_bt, 1, wx.ALL, 5)

        self.time_bt = wx.Button(self, wx.ID_ANY, u"定时任务", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer13.Add(self.time_bt, 1, wx.ALL, 5)

        bSizer10.Add(bSizer13, 1, wx.EXPAND, 5)

        bSizer1.Add(bSizer10, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.h3c_radioBtn.Bind(wx.EVT_RADIOBUTTON, self.h3c_click)
        self.cisco_radioBtn.Bind(wx.EVT_RADIOBUTTON, self.cisco_click)
        self.ruijie_radioBtn.Bind(wx.EVT_RADIOBUTTON, self.ruijie_click)
        self.hw_radioBtn.Bind(wx.EVT_RADIOBUTTON, self.hw_click)
        self.import_config.Bind(wx.EVT_BUTTON, self.import_cfg_click)
        self.clear.Bind(wx.EVT_BUTTON, self.clear_cfg_click)
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
    devCfgPath = ""
    ipCfgPath = ""

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def h3c_click(self, event):
        dev_Type = deviceType.Device.H3C

    def cisco_click(self, event):
        dev_Type = deviceType.Device.CISCO

    def ruijie_click(self, event):
        dev_Type = deviceType.Device.RUIJIE

    def hw_click(self, event):
        dev_Type = deviceType.Device.HW

    def import_cfg_click(self, event):
        dlg = wx.FileDialog(self, u'选择要打开的txt文件', style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            devCfgPath = dlg.GetPath()
            self.read_dev_config(dlg.GetPath())
            dlg.Destroy()

    def clear_cfg_click(self, event):
        self.config_content.SetValue("")

    def import_ip_click(self, event):
        dlg = wx.FileDialog(self, u'选择要打开的txt文件', style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            file = open(dlg.GetPath(), encoding="utf-8")
            self.input_ip_tv.SetValue(dlg.GetPath())
            ipCfgPath = dlg.GetPath()
            file.close()
            dlg.Destroy()

    def clear_ip_path_click(self, event):
        # event.Skip()
        self.input_ip_tv.SetValue("")

    def telnet_click(self, event):
        self.isTelnet = 1

    def ssh_click(self, event):
        self.isSSH = 1

    def start_backup_click(self, event):
        autocheck_net.chech_dev(self.input_ip_tv.GetValue(), self.devCfgPath, self.isSSH, self.isTelnet, dev_Type)

    def time_task_click(self, event):
        event.Skip()

    def read_dev_config(self, path):
        f = open(path, "rb")
        lines = f.readlines()
        print(type(lines))
        for line in lines:
            self.config_content.AppendText(line)
        f.close()


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame2(None)
    frame.Show()
    app.MainLoop()
