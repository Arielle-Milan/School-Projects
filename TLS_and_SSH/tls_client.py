

import socket
import ssl

HOST = '127.0.0.1'
PORT = 65433

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

with socket.create_connection((HOST, PORT)) as client_socket:
    with context.wrap_socket(client_socket, server_hostname=HOST) as secure_socket:
        print(f"Connected securely to {HOST}:{PORT}")
        while True:
            message = input("Enter message (or 'exit' to quit): ")
            if message.lower() == 'exit':
                break
            secure_socket.sendall(message.encode())
            response = secure_socket.recv(1024).decode()
            print(f"Received: {response}")
