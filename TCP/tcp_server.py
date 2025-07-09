import socket
import subprocess

HOST = '127.0.0.1'
PORT = 65432

def execute_command(command):
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        output = e.output
    return output

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Server listening on {HOST}:{PORT}")
    conn, addr = server_socket.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            command = conn.recv(1024).decode()
            if not command or command.lower() == 'exit':
                break
            output = execute_command(command)
            conn.sendall(output)