# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 14:23:38 2025

@author: atcha
"""

import socket
import ssl

HOST = '127.0.0.1'
PORT = 65433

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile="server.crt", keyfile="server.key")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"Secure server listening on {HOST}:{PORT}")
    with context.wrap_socket(server_socket, server_side=True) as secure_socket:
        conn, addr = secure_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)
