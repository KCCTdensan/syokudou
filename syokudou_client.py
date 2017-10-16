#coding: UTF-8
from tkinter import *
import socket
import sys

def key(event):
    try:
        student_id=student_id_textbox.get()
        if not student_id:
                return
        sock=socket.create_connection(("localhost",55555),timeout=3)
        sock.sendall(student_id.encode())
        message_label_text.set(sock.recv(1024).decode())
        root.after(2000,lambda:message_label_text.set(""))
    except BaseException as ex:       
        message_label_text.set(ex)
    finally:
        student_id_textbox_text.set("")

root = Tk()
#root.attributes("-zoomed", "1") #Linux
root.state("zoomed") #Windows
message_label_text = StringVar()
message_label = Label(root,textvariable=message_label_text,font = ("",40),wraplength="25c") #TODO:cと書く公式ドキュメント探し途中
message_label.pack(side=TOP,fill=Y,expand=1)
student_id_textbox_text = StringVar()
student_id_textbox = Entry(root,bd=5,width = 10,textvariable=student_id_textbox_text)
student_id_textbox.pack()
student_id_textbox.bind("<Return>",key)
student_id_textbox.focus_set()

root.mainloop()
