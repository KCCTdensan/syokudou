import socket
import sys
import tkinter

root=tkinter.Tk()
root.title("食堂利用管理システム")


message=tkinter.Label()
message.pack()

def attend(student_id):
	print(student_id)

student_id_textbox=tkinter.Entry()
student_id_textbox.bind("<Key-RETURN>",attend)
student_id_textbox.pack()

root.mainloop()

while True:
    try:
        student_id=input()
        sock=socket.socket()
        sock.connect(("localhost",55555))
        sock.sendall(student_id.encode())
        print(sock.recv(1024).decode())
    except ConnectionResetError:
        print("接続が切断されました．LANケーブル，ハブの電源を確認して下さい．")
    except BaseException  as ex:       
        #TODO:BaseException必須?
        print(ex+"原因不明の例外です．")

