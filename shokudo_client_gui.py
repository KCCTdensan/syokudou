#coding: UTF-8

import wx


class gui():
    def __init__(self):
        font=wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        self.eventprocess.textbox.SetFont(font)
        sizer=wx.FlexGridSizer(cols=2, vgap=1, hgap=5)
        sizer.Add(self.eventprocess.textbox,flag=wx.EXPAND)
        self.frame.SetSizer(sizer)
