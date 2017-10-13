#coding: UTF-8
from shokudo_client_gui import gui
from tkinter import *
import socket
import sys


def key(event):
    try:
        student_id=student_id_textbox.get()
        if not student_id:
                return
        sock=socket.socket()
        #sock.connect(("192.168.11.8",55555))
        #sock.sendall(student_id.encode())
        #message_label_text.set(sock.recv(1024).decode())
        student_id_textbox_text.set("")
    except ConnectionResetError:
        print("接続が切断されました．LANケーブル，ハブの電源を確認して下さい．")
    except BaseException  as ex:       
        #TODO:BaseException必須?
        print(ex+"原因不明の例外です．")
        

if __name__=='__main__':
    gui=gui()
    gui.mainloop()

#top = Tk()
#message_label_text = StringVar()
#message_label = Label(top,textvariable=message_label_text,font = ("",40))
#message_label.pack(side=TOP,fill=Y,expand=1)
#student_id_textbox_text = StringVar()
#student_id_textbox = Entry(top,bd=5,width = 10,textvariable=student_id_textbox_text)
#student_id_textbox.pack()
#student_id_textbox.bind("<Return>",key)

#top.mainloop()
