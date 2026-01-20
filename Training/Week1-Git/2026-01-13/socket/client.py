import socket
import threading

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(("127.0.0.1", 12345))

def message_sending():
    print("Enter your message: ")
    while True:
        try:
            message = input()
            client_socket.send(message.encode("utf-8"))
        except:
            print("Disconnected with server")
            client_socket.close()


threading.Thread(target=message_sending).start()


while True:
    data = client_socket.recv(1024)
    if not data:
        print("Server disconnected")
        break
    message = data.decode("utf-8")
    print(message)

