#coding: UTF-8

import wx
from shokudo_client_event import event


class gui():
    def __init__(self):
        self.eventprocess=event();

        self.app=wx.App()
        self.frame=wx.Frame(None)

        self.frame.Maximize()
        self.frame.SetTitle(u"食堂管理システム")

        self.textbox=wx.TextCtrl(self.frame,wx.ID_ANY)

        self.frame.Bind(wx.EVT_KEY_DOWN,self.eventprocess.onEVT_KEY_DOWN)
        self.frame.Bind(wx.EVT_KEY_UP,self.eventprocess.onEVT_KEY_UP)
        
        self.app.SetTopWindow(self.frame)
        self.frame.Show(True)

    def mainloop(self):
        self.app.MainLoop()