# coding: UTF-8

import wx
import socket


string=u""

def onEVT_TEXT_ENTER(evt):
    try:
        student_id=textbox.GetValue()
        if not student_id:
            return
        sock=socket.socket()
        sock.connect(("192.168.11.8",55555))
        sock.sendall(student_id.encode())
        message_label_text.set(sock.recv(1024).decode())
        textbox.Clear()

    except ConnectionResetError:
        #print(u"�ڑ����ؒf����܂����DLAN�P�[�u���C�n�u�̓d�����m�F���ĉ������D")
        print(u"setsudan")

    except BaseException  as ex:       
        #TODO:BaseException�K�{?
        #print(ex+u"�����s���̗�O�ł��D")
        print(u"reigai")


app=wx.App()
frame=wx.Frame(None)

frame.Maximize()
frame.SetTitle(u"shokudo-kanri-system")

textbox=wx.TextCtrl(frame,wx.ID_ANY,style=wx.TE_PROCESS_ENTER)
textbox.Bind(wx.EVT_TEXT_ENTER,onEVT_TEXT_ENTER)
textbox.SetMaxLength(16)

font=wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
textbox.SetFont(font)
sizer=wx.FlexGridSizer(cols=2, vgap=1, hgap=5)
sizer.Add(textbox,flag=wx.EXPAND)
frame.SetSizer(sizer)

app.SetTopWindow(frame)
frame.Show(True)

app.MainLoop()