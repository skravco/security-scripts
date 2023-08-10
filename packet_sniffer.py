# Import necessary modules from scapy.
from scapy.all import sniff, IP, TCP

# Define a function 'process_packet' to handle each captured packet.
# Argument:
#     packet: The packet captured by scapy sniffing.


def process_packet(packet):
    # Check if the packet has a TCP layer.
    if packet.haslayer(TCP):
        # Extract the IP and TCP layers from the packet.
        ip_layer = packet.getlayer(IP)
        tcp_layer = packet.getlayer(TCP)

        # Print the source and destination IP addresses.
        print(f'source IP: {ip_layer.src}, destination IP: {ip_layer.dst}')

        # Print the source and destination port numbers.
        print(
            f'source port: {tcp_layer.sport}, destination port: {tcp_layer.dport}')

        # Print the TCP flags.
        print(f'TCP Flag: {tcp_layer.flags}')

        # Print a separator line.
        print('---- ---- ---- ---- ---- ---- ---- ----')


# Start sniffing packets with the following options:
# - 'count=10': Capture 10 packets.
# - 'prn=process_packet': Call the 'process_packet' function for each captured packet.
# - 'lfilter=lambda p: p.haslayer(TCP)': Filter packets to only capture those that have a TCP layer.
sniff(count=10, prn=process_packet, lfilter=lambda p: p.haslayer(TCP))
