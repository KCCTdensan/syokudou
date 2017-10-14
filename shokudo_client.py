#coding:UTF-8

import wx
import socket
import sys


message={
    b"SUCCEEDED":"ご利用ありがとうございます。",
    b"INVALID_ID":"不正な学籍番号です。",
    b"DUPLICATED":"多重利用です。"
}

def onEVT_TEXT_ENTER(evt):
    try:
        student_id=textbox.GetValue()
        if not student_id:
            message_label_text.SetLabel("学籍番号を入力してください")
            return
        sock=socket.socket()
        #sock.connect(("192.168.11.8",55555))
        sock.connect(("localhost",55555))
        sock.sendall(student_id.encode())
        error_code=sock.recv(1024)

        message_label_text.SetLabel(message[error_code])
        textbox.Clear()

    except ConnectionResetError:
        print("接続が切断されました。LANケーブル、ハブの電源を確認して下さい。")
        wx.MessageBox("接続が切断されました。LANケーブル、ハブの電源を確認して下さい。",style=wx.OK)
        textbox.Clear()

    except BaseException  as ex:       
        #TODO:BaseException必須?
        print("原因不明の例外です．")
        wx.MessageBox("プログラムで原因不明の例外が発生しました。",style=wx.OK)
        textbox.Clear()


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