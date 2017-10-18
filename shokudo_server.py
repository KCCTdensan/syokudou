import socket
import re
import datetime
    

customers=[]

with socket.socket()as listen_sock:
    listen_sock.bind(("",55555))
    listen_sock.listen()
    with open("log.csv","a") as csvfile:
        while True:
            try:
                client_sock,addr=listen_sock.accept()
                student_id=client_sock.recv(1024).decode()
                csvfile.write(str(datetime.datetime.today())+","+student_id+"\n")
                print(student_id)
                if re.match(r"\d{6}$",student_id):
                    if student_id in customers:
                        client_sock.sendall(b"DUPLICATED")
                    else:
                        customers.append(student_id)
                        client_sock.sendall(b"SUCCEEDED")
                else:
                    client_sock.sendall(b"INVALID_ID")
            except BaseException  as ex:
                print(ex)
