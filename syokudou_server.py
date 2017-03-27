#TODO:log残すとか統計取るとか
#TODO:停電対策(耐障害)

import socket
import re
import csv
import datetime

customers=[]

listen_sock=socket.socket()
listen_sock.bind(("",55555))
listen_sock.listen()
with open("log.csv","a",newline="") as csvfile:
    while True:
        try:
            client_sock,addr=listen_sock.accept()
            command=client_sock.recv(1024).decode()
            print(command)
            #csv_writer = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
            #csv_writer.writerow([str(date.today()),command])

            #    customers.clear()
            #    client_sock.sendall("利用履歴を削除しました．".encode())
            if re.match(r"\d{6}$",command):
                if command in customers:
                    client_sock.sendall("多重利用です!!!!!".encode())
                else:
                    customers.append(command)
                    client_sock.sendall(b"ok")
            else:
                client_sock.sendall("不正な学生証です．".encode())
        except ConnectionResetError:
            print("接続が切断されました．LANケーブル，ハブの電源を確認して下さい．")
        except BaseException  as ex:
            print(ex+"原因不明の例外です．")
            
#TODO:listen_sock.close()
