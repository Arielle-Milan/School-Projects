import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    while True:
        command = input("Enter command to execute (or 'exit' to quit): ")
        client_socket.sendall(command.encode())
        if command.lower() == 'exit':
            break
        output = client_socket.recv(4096).decode()
        print(f"Output:\n{output}")
