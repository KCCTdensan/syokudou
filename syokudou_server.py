#TODO:停電対策(耐障害)

import socket
import re
import csv
import datetime

customers=[]

def save(n):
    """
    save
    customers.jsonに指定文字列,日付を書き込む
    それだけ
    """
    r = open('customers.json','a')
    r.write(str(n) + ":" + str(datetime.date.today()) + "\n")
    r.close()
def load():
    """
    load
    この関数を呼び出したときと同日にsaveされた記録をすべてcustomerに書き込む
    それだけ
    """
    r = open('customers.json','r')
    for toCust in  r.readlines():
        if toCust[7:17] == str(datetime.date.today()):
            customers.append(toCust[0:6])
    r.close()

with socket.socket()as listen_sock:
    listen_sock.bind(("",55555))
    listen_sock.listen(1)
    load()
    with open("log.csv","a") as csvfile:
        while True:
            try:
                client_sock,addr=listen_sock.accept()
                student_id=client_sock.recv(1024).decode()
                csvfile.write(str(datetime.datetime.today())+","+student_id+"\n")
                print(student_id)
                if re.match(r"\d{6}$",student_id):
                    if student_id in customers:
                        client_sock.sendall("多重利用です!!!!!".encode())
                    else:
                        customers.append(student_id)
                        save(student_id)
                        client_sock.sendall(b"ok")
                else:
                    client_sock.sendall("不正な学生証です．".encode())
            except ConnectionResetError:
                print("接続が切断されました．LANケーブル，ハブの電源を確認して下さい．")
            except BaseException  as ex:
                print(ex+"原因不明の例外です．")