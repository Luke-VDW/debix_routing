# client.py
import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(("localhost", 8888))

# Send a message to the server
message = "Hello, TCP Server!"
client_socket.send(message.encode())

# Receive the server's response
response = client_socket.recv(1024)
print(f"Received from server: {response.decode()}")

# Close the client socket
client_socket.close()