# server.py
import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind(("0.0.0.0", 8888))

# Listen for incoming connections
server_socket.listen(5)

print("Server listening on port 8888")

while True:
    # Accept a connection
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")

    # Receive data from the client
    data = client_socket.recv(1024)
    if not data:
        break

    print(f"Received: {data.decode()}")

    # Send the data back to the client
    client_socket.send(data)

    # Close the client socket
    client_socket.close()

# Close the server socket
server_socket.close()
