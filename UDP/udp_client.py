
import socket
import threading

HOST = '127.0.0.1'
PORT = 12345

def receive_messages(client_socket):
    while True:
        try:
            message, _ = client_socket.recvfrom(1024)
            print(f"\n{message.decode()}\n> ", end="")
        except:
            break

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
    client_socket.connect((HOST, PORT))
    threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()
    while True:
        message = input("> ")
        if message.lower() == 'exit':
            break
        client_socket.sendto(message.encode(), (HOST, PORT))
