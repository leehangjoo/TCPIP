import socket
import threading
import sqlite3
from tkinter import *
from tkinter.scrolledtext import ScrolledText

def Send(client_sock):
    while True:
        send_data = bytes(input().encode()) # 사용자 입력
        client_sock.send(send_data)  # 사용자 -> Server 데이터 송신

def Recv(client_sock):
    while True:
        recv_data = client_sock.recv(1024).decode()  # 사용자 -> Client 데이터 수신
        print(recv_data)
        

#Interface
def initialize_gui(client_sock):
    client_sock.root = Tk()
    fr = []
    for i in range(0,5):
        fr.append(Frame(client_sock.root))
        fr[i].pack(fill=BOTH)
    client_sock.name_label = Label(fr[0], text='채팅 프로그래밍')
    client_sock.recv_label = Label(fr[1], text='수신 메시지:')
    client_sock.chat_transcript_area = ScrolledText(fr[2], height =20, width=60)
    client_sock.name_label.pack(side=LEFT)
    client_sock.recv_label.pack(side=LEFT)
    client_sock.chat_transcript_area.pack(side=LEFT, padx=2, pady=2)



#TCP Client
if __name__ == '__main__':
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP Socket
    Host = 'localhost' #통신할 대상의 IP 주소
    Port = 8080  #통신할 대상의 Port 주소
    client_sock.connect((Host, Port)) #서버로 연결시도
    print('연결 중  ', Host, Port)
    One = 0
    conn = sqlite3.connect("final.db")
    cur = conn.cursor()
    if One == 1:
        conn.execute('CREATE TABLE idsave_data(name TEXT)')
    

    #Client의 메시지를 보낼 쓰레드
    thread1 = threading.Thread(target=Send, args=(client_sock, ))
    thread1.start()

    #Server로 부터 다른 클라이언트의 메시지를 받을 쓰레드
    thread2 = threading.Thread(target=Recv, args=(client_sock, ))
    thread2.start()
