import socket

HOST = '127.0.0.1'
PORT = 12345
clients = set()

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
    server_socket.bind((HOST, PORT))
    print(f"Server listening on {HOST}:{PORT}")
    while True:
        message, client_address = server_socket.recvfrom(1024)
        if client_address not in clients:
            clients.add(client_address)
        print(f"Received message from {client_address}: {message.decode()}")
        for client in clients:
            if client != client_address:
                server_socket.sendto(message, client)