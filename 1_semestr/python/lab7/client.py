import socket

PORT = 50007
while True:
    mail = input("Введите email-адрес: ")
    text = input("Введите текст сообщения: ")
    mt = mail + ":" + text
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', PORT))
        s.sendall(mt.encode())
        data = s.recv(1024)
        if data.decode() == "OK":
            break
    print('Received', repr(data))
