#coding: UTF-8
import wx

from shokudo_client_event import event


class gui():
    def __init__(self):
        self.eventprocess=event();

        self.app=wx.App()
        self.frame=wx.Frame(None)

        self.size=wx.ScreenDC().GetSize()
        self.frame.SetSize(self.size)
        self.frame.SetPosition(wx.Point(0,0))

        self.frame.SetTitle(u'shokudo-kanri-system')

        self.frame.Bind(wx.EVT_KEY_DOWN,self.eventprocess.onEVT_KEY_DOWN)
        self.frame.Bind(wx.EVT_KEY_UP,self.eventprocess.onEVT_KEY_UP)

        self.app.SetTopWindow(self.frame)
        self.frame.Show(True)

    def mainloop(self):
        self.app.MainLoop()