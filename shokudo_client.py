#coding: UTF-8

import wx
import socket


string=u""

def onEVT_TEXT_ENTER(evt):
    try:
        student_id=textbox.GetValue()
        if not student_id:
            return
        #sock=socket.socket()
        #sock.connect(("192.168.11.8",55555))
        #sock.sendall(student_id.encode())
        #message_label_text.SetLabel(sock.recv(1024).decode())
        message_label_text.SetLabel(u"Input:"+student_id)
        textbox.Clear()

    except ConnectionResetError:
        #print(u"接続が切断されました．LANケーブル，ハブの電源を確認して下さい．")
        print(u"setsudan")

    except BaseException  as ex:       
        #TODO:BaseException必須?
        #print(ex+u"原因不明の例外です．")
        print(u"reigai")

        
app=wx.App()
frame=wx.Frame(None)

frame.Maximize()
frame.SetTitle(u"shokudo-kanri-system")

font=wx.Font(100, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)

textbox=wx.TextCtrl(frame,wx.ID_ANY,style=wx.TE_PROCESS_ENTER)
textbox.Bind(wx.EVT_TEXT_ENTER,onEVT_TEXT_ENTER)
textbox.SetFont(font)
textbox.SetMaxLength(16)

student_id_label_text=wx.StaticText(frame,-1,u"gakusekiNo")
student_id_label_text.SetFont(font)

message_label_text=wx.StaticText(frame,wx.ID_ANY,u"gakusekiNo wo nyuuryoku sitekudasai")
message_label_text.SetFont(font)

vsizer=wx.BoxSizer(wx.VERTICAL)

hsizer=wx.BoxSizer(wx.HORIZONTAL)
hsizer.Add(student_id_label_text)
hsizer.Add(textbox,proportion=1)

vsizer.Add(hsizer,flag=wx.EXPAND|wx.ALIGN_CENTER|wx.RIGHT|wx.LEFT|wx.TOP,border=100)
vsizer.Add(message_label_text,flag=wx.RIGHT|wx.LEFT,border=100)

frame.SetSizer(vsizer)

#sizer=wx.FlexGridSizer(cols=2, vgap=1, hgap=5)
#sizer.Add(textbox,flag=wx.GROW)
#frame.SetSizer(sizer)

app.SetTopWindow(frame)
frame.Show(True)

app.MainLoop()