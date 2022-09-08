import socket
import threading
print(socket.gethostbyname(socket.gethostname()))

nickname = input("Enter nick name ? : ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('HOST IP ADDRESS', "HOST PORT(int)"))


def receive():
    while True:
        message = client.recv(1024).decode('utf-8')
        if message == 'Nickname : ':
            client.send(nickname.encode('utf-8'))
        else:
            print(message)

def sendMessage():
    while True:
        girdi = input("")
        if girdi == "Exit":
            message = '{} left ...'.format(nickname)
            client.send(message.encode("utf-8"))
            client.close()
        message = '{}: {}'.format(nickname,girdi)
        client.send(message.encode('utf-8'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=sendMessage)
write_thread.start()