import socket
import threading

def forward_data(src_sock, dest_sock):
    """
    Forward data from source socket to destination socket.

    :param src_sock: Source socket.
    :param dest_sock: Destination socket.
    """
    while True:
        data = src_sock.recv(1024)
        if not data:
            break
        dest_sock.send(data)

def handle_client(client_sock):
    """
    Handle communication between client and remote server.

    :param client_sock: Client socket.
    """
    # Connect to the remote server
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.connect(('remote_server', 80))

    # Start threads for forwarding data in both directions
    client_thread = threading.Thread(target=forward_data, args=(client_sock, server_sock))
    server_thread = threading.Thread(target=forward_data, args=(server_sock, client_sock))

    client_thread.start()
    server_thread.start()

    # Wait for threads to complete
    client_thread.join()
    server_thread.join()

    # Close sockets
    client_sock.close()
    server_sock.close()

def main():
    """
    Main function to set up a local socket server.
    """
    local_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    local_sock.bind(('0.0.0.0', 8080))
    local_sock.listen(5)

    while True:
        client_sock, _ = local_sock.accept()
        handle_thread = threading.Thread(target=handle_client, args=(client_sock,))
        handle_thread.start()

if __name__ == '__main__':
    main()


 