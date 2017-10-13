#coding: utf-8
import wx

class GUI():
    def __init__(self):
        self.string=[]

        self.app=wx.App()
        self.frame=wx.Frame(None)

        self.size=wx.ScreenDC().GetSize()
        self.frame.SetSize(self.size)
        self.frame.SetPosition(wx.Point(0,0))

        self.frame.SetTitle(u'shokudo-kanri-system')

        self.frame.Bind(wx.EVT_KEY_DOWN,onEVT_KEY_DOWN)
        self.frame.Bind(wx.EVT_KEY_UP,onEVT_KEY_UP)

        self.app.SetTopWindow(self.frame)
        self.frame.Show(True)

    def mainloop(self):
        self.app.MainLoop()

    def onEVT_KEY_DOWN(self,event):
        self.string+=event.GetKeyCode()

    def onEVT_KEY_UP(self,event):
        print(self.string)