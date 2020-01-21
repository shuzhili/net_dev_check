# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 10:25:50 2018
@author: William_Yue91
"""

import wx
import wx.grid
import wx.adv


class countone(wx.Frame):
    def __init__(self, parent=None, idnum=-1, UpdateUI=None):
        wx.Frame.__init__(self, parent, idnum, title='个人统计', size=(1000, 800), pos=(200, 200))
        self.UpdateUI = UpdateUI
        self.pnl = wx.Panel(self)
        self.InitUI()

    def InitUI(self):
        logo_title = wx.StaticText(self.pnl, -1, '统计请确认', pos=(180, 220))
        logo_title.SetForegroundColour('#0a74f7')
        titleFont = wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.BOLD, True)
        logo_title.SetFont(titleFont)

        font = wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.BOLD, True)

        startLabel = wx.StaticText(self.pnl, -1, '起始', pos=(50, 40))
        startLabel.SetFont(font)

        yearLabel1 = wx.StaticText(self.pnl, -1, '年', pos=(250, 40))
        yearLabel1.SetFont(font)
        self.yearInput1 = wx.TextCtrl(self.pnl, -1, u'', pos=(190, 40), size=(60, -1))
        self.yearInput1.SetForegroundColour('gray')
        self.yearInput1.SetFont(font)

        monthLabel1 = wx.StaticText(self.pnl, -1, '月', pos=(330, 40))
        monthLabel1.SetFont(font)
        self.monthInput1 = wx.TextCtrl(self.pnl, -1, u'', pos=(290, 40), size=(40, -1))
        self.monthInput1.SetForegroundColour('gray')
        self.monthInput1.SetFont(font)

        dayLabel1 = wx.StaticText(self.pnl, -1, '日', pos=(410, 40))
        dayLabel1.SetFont(font)
        self.dayInput1 = wx.TextCtrl(self.pnl, -1, u'', pos=(370, 40), size=(40, -1))
        self.dayInput1.SetForegroundColour('gray')
        self.dayInput1.SetFont(font)

        endLabel = wx.StaticText(self.pnl, -1, '结束', pos=(50, 80))
        endLabel.SetFont(font)

        yearLabel2 = wx.StaticText(self.pnl, -1, '年', pos=(250, 80))
        yearLabel2.SetFont(font)
        self.yearInput2 = wx.TextCtrl(self.pnl, -1, u'', pos=(190, 80), size=(60, -1))
        self.yearInput2.SetForegroundColour('gray')
        self.yearInput2.SetFont(font)

        monthLabel2 = wx.StaticText(self.pnl, -1, '月', pos=(330, 80))
        monthLabel2.SetFont(font)
        self.monthInput2 = wx.TextCtrl(self.pnl, -1, u'', pos=(290, 80), size=(40, -1))
        self.monthInput2.SetForegroundColour('gray')
        self.monthInput2.SetFont(font)

        dayLabel2 = wx.StaticText(self.pnl, -1, '日', pos=(410, 80))
        dayLabel2.SetFont(font)
        self.dayInput2 = wx.TextCtrl(self.pnl, -1, u'', pos=(370, 80), size=(40, -1))
        self.dayInput2.SetForegroundColour('gray')
        self.dayInput2.SetFont(font)

        self.edtDateb = wx.adv.DatePickerCtrl(self.pnl, id=-1, size=(90, 40), pos=(90, 30),
                                              style=wx.adv.DP_DROPDOWN | wx.adv.DP_SHOWCENTURY)
        self.Bind(wx.adv.EVT_DATE_CHANGED, self.OnCalSelChangedb, self.edtDateb)

        self.edtDatee = wx.adv.DatePickerCtrl(self.pnl, id=-1, size=(90, 40), pos=(90, 70),
                                              style=wx.adv.DP_DROPDOWN | wx.adv.DP_SHOWCENTURY)
        self.Bind(wx.adv.EVT_DATE_CHANGED, self.OnCalSelChangede, self.edtDatee)

        # 统计确认
        startButton = wx.Button(self.pnl, -1, u'开始', pos=(90, 160), size=(120, 40))
        startButton.SetBackgroundColour('white')
        startButton.SetForegroundColour('black')
        self.Bind(wx.EVT_BUTTON, self.sureEvent, startButton)

        # 返回功能界面
        returnButton = wx.Button(self.pnl, -1, u'返回', pos=(240, 160), size=(120, 40))
        returnButton.SetBackgroundColour('black')
        returnButton.SetForegroundColour('#ffffff')
        self.Bind(wx.EVT_BUTTON, self.cancleEvent, returnButton)

        self.Show()

    def OnCalSelChangedb(self, event):
        cal = event.GetEventObject()
        datestr = cal.GetValue()
        beginyear = datestr.year
        beginmonth = str(int(datestr.month) + 1)
        beginday = datestr.day

        self.yearInput1.Clear()
        self.monthInput1.Clear()
        self.dayInput1.Clear()

        self.yearInput1.WriteText(str(beginyear))
        self.monthInput1.WriteText(str(beginmonth))
        self.dayInput1.WriteText(str(beginday))

    def OnCalSelChangede(self, event):
        cal = event.GetEventObject()
        datestr = cal.GetValue()
        endyear = datestr.year
        endmonth = str(int(datestr.month) + 1)
        endday = datestr.day

        self.yearInput2.Clear()
        self.monthInput2.Clear()
        self.dayInput2.Clear()

        self.yearInput2.WriteText(str(endyear))
        self.monthInput2.WriteText(str(endmonth))
        self.dayInput2.WriteText(str(endday))

    def sureEvent(self, event):
        yearbegin = self.yearInput1.GetValue()
        monthbegin = self.monthInput1.GetValue()
        daybegin = self.dayInput1.GetValue()

        yearend = self.yearInput2.GetValue()
        monthend = self.monthInput2.GetValue()
        dayend = self.dayInput2.GetValue()

        print("begin:", yearbegin, monthbegin, daybegin)
        print("end:", yearend, monthend, dayend)

    def cancleEvent(self, event):
        self.Destroy()


if __name__ == '__main__':
    app = wx.App()
    frame = countone()
    app.MainLoop()