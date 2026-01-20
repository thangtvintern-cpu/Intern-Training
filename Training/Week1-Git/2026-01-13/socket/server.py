
import threading
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 12345))
server_socket.listen()
print("Listening on 127.0.0.1:12345")


clients_info = dict()
client_number = 1

# Gửi message cho toàn bộ client
def broadcast(message,sender):
    for sock,name in clients_info.items():
        if sock != sender:
            sock.send((name + ": " + message).encode("utf-8"))
        else:
            sock.send(("You: " + message).encode("utf-8"))

# Xử lý client cho mỗi thread riêng
def client_handler(client_socket):
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                print("Client disconnected")
                break
            message = data.decode("utf-8")
            print(clients_info[client_socket] + ": " + message)
            broadcast(message,client_socket)
        except:
            print("Disconnected with :" + clients_info[client_socket])
            client_socket.close()
            del clients_info[client_socket]
            break


# Main thread chạy      
while True:
    client_socket, addr = server_socket.accept()
    # Thêm client vào dictionary
    if (client_socket not in clients_info.keys()):
        clients_info[client_socket] = "User" + str(client_number)

        # khi client socket kết nối đến sẽ tạo thread riêng để xử lý
        threading.Thread(target=client_handler, args=(client_socket,)).start()

        print(f"Connected by {addr}")
        client_number += 1
    
    
    
    
