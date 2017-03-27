import socket

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
