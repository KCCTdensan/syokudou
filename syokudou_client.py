from tkinter import *
import socket
import os
import datetime

deadline=datetime.datetime(2018,11,3)

def key(event):
    try:
        student_id=student_id_textbox.get()
        if not student_id:
                return
        if student_id=="poweroff":
            os.system("poweroff")
        sock=socket.create_connection(("192.168.11.8",55555),timeout=3)
        sock.sendall(student_id.encode())
        message_label_text.set(sock.recv(1024).decode())
        root.after(2000,lambda:message_label_text.set(""))
    except BaseException as ex:       
        message_label_text.set(ex)
    finally:
        student_id_textbox_text.set("")

root = Tk()
root.attributes("-fullscreen", True)
root.config(cursor="none")
message_label_text = StringVar()
message_label = Label(root,textvariable=message_label_text,font = ("",40),wraplength="25c") #TODO:cと書く公式ドキュメント探し途中
message_label.pack(side=TOP,fill=Y,expand=1)
student_id_textbox_text = StringVar()
student_id_textbox = Entry(root,bd=5,width = 10,textvariable=student_id_textbox_text)
student_id_textbox.pack()
student_id_textbox.bind("<Return>",key)
student_id_textbox.focus_set()
countdown_label_text = StringVar()
countdown_label = Label(None,text="高専祭まであと"+str((deadline-datetime.datetime.now()).days+1)+"日",font = ("",40))
countdown_label.pack(side=TOP,fill=Y,expand=1,padx=5, pady=5)

root.mainloop()
