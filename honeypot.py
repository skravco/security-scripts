import socket
import threading 

def handle_client(client_socket, addr):
    """
    This function handles communication with a connected client.

    :param client_socket: The socket object for the connected client.
    :param addr: The address of the connected client.
    """
    client_socket.send(b'SSH-2.0-OpenSSH_7.4\r\n')

    # Receive and display data from the client
    data = client_socket.recv(1024)
    print('received: ', data.decode())

    # Send username prompt and receive attempted username
    client_socket.send(b'username: ')
    username = client_socket.recv(1024).decode().strip()
    print('attempted username: ', username)

    # Send password prompt and receive attempted password
    client_socket.send(b'password: ')
    password = client_socket.recv(1024).decode().strip()
    print('attempted password: ', password)

    # Inform the client of access denial and close the connection
    client_socket.send(b'access denied \r\n')
    client_socket.close()
    print(f'connection from {addr} closed.')

def main():
    """
    The main function to set up the server and accept incoming connections.
    """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 8080)) 
    server.listen(5) 
    print('listening on port 8080...')  

    while True:
        client, addr = server.accept()
        print(f'accepted connection from {addr}')
        client_thread = threading.Thread(target=handle_client, args=(client, addr))
        client_thread.start()

if __name__ == '__main__':
    main()
