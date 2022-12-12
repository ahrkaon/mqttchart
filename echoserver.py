#TCP_echoserver.py
# 송수신 예외 처리를 한 에코 서버 프로그램

from socket import *
import os
port = 9000
BUFSIZE = 1024
file_list = os.listdir(os.getcwd())

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(5) #최대 대기 클라이언트 수
print("Waiting for clients...")
c_sock, (r_host, r_port) = sock.accept()
print('connected by', r_host, r_port)
while True:
    # 수신 예외 처리
    try:
        f =  open("test.csv", 'a')
        data = c_sock.recv(BUFSIZE)
        if not data: #연결 해제됨
            c_sock.close()
            print('연결이 정상적으로 종료되었습니다')
            break
    except:
        print("연결이 강제로 종료되었습니다")
        c_sock.close() #소켓을 닫는다
        break #무한 루프 종료
    else:
        f.write(data.decode())
        print(data.decode())
        
    # 송신 예외 처리
    try:
        c_sock.send(data)
    except: #연결 종료로 인한 예외 발생
        print("연결이 종료되었습니다")
        c_sock.close() #소켓을 닫는다
        break #무한 루프 종료