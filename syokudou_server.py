import socket
import re
import datetime

#customers=[]

with socket.socket() as listen_sock:
    listen_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_sock.bind(("",55555))
    listen_sock.listen(1)
    csvfile = open(str(datetime.datetime.now().date().today())+"log.txt","r")
    studentIDsStr = csvfile.read();
    customers = studentIDsStr.split("\n") 
    while True:
        try:            
            client_sock,addr=listen_sock.accept()
            student_id=client_sock.recv(1024).decode()
            print(student_id)
            if re.match(r"\d{6}$",student_id):
                if student_id in customers:
                    client_sock.sendall("多重利用です!!!!!".encode())
                else:
                    customers.append(student_id)
                    client_sock.sendall(b"ok")
            else:
                client_sock.sendall("不正な学生証です．".encode())
            csvfile = open(str(datetime.datetime.now().date().today())+"log.txt","a")
            csvfile.write(student_id+"\n")
            csvfile.close()
        except BaseException as ex:
            print(ex)
