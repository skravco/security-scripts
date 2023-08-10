import socket

# Define a function 'scan_ports' that will scan for open ports within a specified range on a given IP address.
# Arguments:
#     ip: The IP address to scan.
#     start_port: The first port in the range to start scanning from.
#     end_port: The last port in the range to end scanning at.


def scan_ports(ip, start_port, end_port):
    # Loop through each port in the specified range.
    for port in range(start_port, end_port + 1):
        # Create a new socket object using IPv4 addressing (AF_INET) and TCP protocol (SOCK_STREAM).
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Set the timeout for the socket connection to 1 second to avoid indefinite blocking.
        s.settimeout(1)

        # Attempt to establish a connection to the IP address and port.
        result = s.connect_ex((ip, port))

        # If 'result' is 0, it means the connection was successful (port is open).
        if result == 0:
            print(f'port {port} is open')

        # Close the socket after attempting the connection.
        s.close()


# Call the 'scan_ports' function with the IP address '127.0.0.1', and scan ports from 1 to 1024.
scan_ports('127.0.0.1', 1, 1024)
