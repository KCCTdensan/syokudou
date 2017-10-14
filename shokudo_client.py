#coding:UTF-8

import wx
import socket
import sys


string=""

def onEVT_TEXT_ENTER(evt):
    try:
        student_id=textbox.GetValue()
        if not student_id:
            return
        sock=socket.socket()
        sock.connect(("192.168.11.8",55555))
        sock.sendall(student_id.encode())
        error_code=sock.recv(1024).decode()
        if error_code=="0":
            message_label_text.SetLabel("ご利用ありがとうございます。")
        elif error_code=="1":
            message_label_text.SetLabel("不正な学籍番号です。")
        elif error_code=="2":
            message_label_text.SetLabel("多重利用です。")

        textbox.Clear()

    except ConnectionResetError:
        print("接続が切断されました．LANケーブル，ハブの電源を確認して下さい．")

    except BaseException  as ex:       
        #TODO:BaseException必須?
        print(ex+"原因不明の例外です．")

        
app=wx.App()
frame=wx.Frame(None)

frame.Maximize()
frame.SetTitle("食堂管理システム")

font=wx.Font(100, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)

textbox=wx.TextCtrl(frame,wx.ID_ANY,style=wx.TE_PROCESS_ENTER)
textbox.Bind(wx.EVT_TEXT_ENTER,onEVT_TEXT_ENTER)
textbox.SetFont(font)
textbox.SetMaxLength(16)

student_id_label_text=wx.StaticText(frame,wx.ID_ANY,"学籍番号:")
student_id_label_text.SetFont(font)

message_label_text=wx.StaticText(frame,wx.ID_ANY,"学籍番号を入力してください")
message_label_text.SetFont(font)

vsizer=wx.BoxSizer(wx.VERTICAL)

hsizer=wx.BoxSizer(wx.HORIZONTAL)
hsizer.Add(student_id_label_text)
hsizer.Add(textbox,proportion=1)

vsizer.Add(hsizer,flag=wx.EXPAND|wx.ALIGN_CENTER|wx.RIGHT|wx.LEFT|wx.TOP,border=100)
vsizer.Add(message_label_text,flag=wx.RIGHT|wx.LEFT,border=100)

frame.SetSizer(vsizer)

app.SetTopWindow(frame)
frame.Show(True)

app.MainLoop()