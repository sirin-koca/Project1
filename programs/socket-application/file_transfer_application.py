"""
DATA2410 - Networks and Cloud Computing - Portfolio2
Assignment: implementing file transfer system using UDP with reliablity.
"""
# Importing the necessary packages:
import socket
import struct
import argparse
import os

# Defining variables which will be used in the program such as  the maximum packet size, the size of the packet
# header, and the maximum size of the data payload:
"""MAX_PACKET_SIZE is set to 1472. This is the maximum size of a packet that will be sent over the network. This 
value is determined by the maximum transmission unit (MTU) of the network, which is the largest amount of data that 
can be transmitted in a single packet. Usually the maximum packet size for UDP is 1472 bytes. This includes the 
header size of 12 bytes (sequence number, acknowledgement number, flags, and receiver window) and application data 
size of 1460 bytes.

The maximum packet size of 1472 bytes is set based on the assumption that the maximum transmission unit (MTU) of the 
network is 1500 bytes, which is the standard for Ethernet networks. This means that the maximum payload size that 
can be transmitted in a single packet over the network is 1500 bytes. However, this includes the size of the IP and 
UDP headers, which are typically 20 and 8 bytes, respectively. Therefore, the maximum size of the payload that can 
be sent in a UDP packet is 1472 bytes (1500 - 20 - 8 = 1472). 

We will add the 20-byte IP header and the 8-byte UDP header to the 1472-byte data payload, we get a total of 1500 bytes, 
which is the maximum size of an Ethernet frame. This means that our packet can be sent over the network without 
fragmentation."""
MAX_PACKET_SIZE = 1472
HEADER_SIZE = struct.calcsize('!IIHH')
MAX_DATA_SIZE = MAX_PACKET_SIZE - HEADER_SIZE
FIN_FLAG = 0b00000010


# Defining a function that will take user input and parse them using the "argparse" module:
def argument_parser():
    parser = argparse.ArgumentParser(description='UDP file transfer with reliability layer')
    parser.add_argument('-c', '--client', action='store_true', help='Start the application as a client')
    parser.add_argument('-s', '--server', action='store_true', help='Start the application as a server')
    parser.add_argument('--host', type=str, help='host to connect to (default: localhost)', default='localhost')
    parser.add_argument('-p', '--port', type=int, help='port to connect to or bind to (default: 5000)', default=5000)
    parser.add_argument('-f', '--file', required=True, help='The path to the file to send or receive')
    parser.add_argument('-b', '--buffer_size', type=int, default=2048, help='Buffer size')
    parser.add_argument('-t', '--timeout', type=int, default=5, help='Timeout in seconds')
    return parser.parse_args()


# Define "create_packet" function. This function takes in the packet header fields (seq, ack, flags, win) and the
# data payload (data) and creates a packet by packing the header using the struct module and concatenating it with
# the data.
"""!IIHH is a format string used by the Python struct module to specify the structure of a binary data. The 
exclamation mark "!" denotes that the byte order is network (big-endian) order. The format string contains four 
parts: "I" stands for an unsigned integer (4 bytes) "I" again stands for an unsigned integer (4 bytes) "H" stands for 
an unsigned short integer (2 bytes) "H" again stands for an unsigned short integer (2 bytes) So the format string 
"!IIHH" means that we have four fields in our packet header: two unsigned integers (seq, ack), followed by two 
unsigned short integers (flags, win), each in big-endian byte order."""


def create_packet(seq, ack, flags, win, data):
    header = struct.pack('!IIHH', seq, ack, flags, win)
    packet = header + data
    return packet


# Define "parse_header" function. This function takes in a packet and extracts the header fields by unpacking the
# header using the struct module.
def parse_header(packet):
    header = packet[:HEADER_SIZE]
    fields = struct.unpack('!IIHH', header)
    return fields


# Define your parse_flags function. This function takes in the flags field of a packet header and extracts the
# individual flag values (SYN, ACK, FIN) using bitwise operations.
def parse_flags(flags):
    syn = flags & (1 << 3)
    ack = flags & (1 << 2)
    fin = flags & (1 << 1)
    return syn, ack, fin


def send_file(host, port, file_path, buffer_size, timeout, ack_flag=None):
    # create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # set timeout
    sock.settimeout(timeout)

    # read the file and send it in chunks
    with open(file_path, 'rb') as file:
        sequence_number = 1
        while True:
            data = file.read(buffer_size)
            if not data:
                break
            packet = create_packet(sequence_number, 0, 0, 0, data)
            sock.sendto(packet, (host, port))
            try:
                ack_packet, server_address = sock.recvfrom(HEADER_SIZE)
                seq, ack, flags, win = parse_header(ack_packet)
                if ack != sequence_number:
                    raise Exception(f"Received unexpected ack number: {ack}")
            except socket.timeout:
                print("Timeout: no response from server")
                continue
            sequence_number += 1

    # send FIN packet to indicate the end of file
    packet = create_packet(sequence_number, 0, FIN_FLAG, 0, b'')
    sock.sendto(packet, (host, port))

    # wait for FIN-ACK packet from server
    try:
        fin_ack_packet, server_address = sock.recvfrom(HEADER_SIZE)
        seq, ack, flags, win = parse_header(fin_ack_packet)
        if flags != (FIN_FLAG | ACK_FLAG):
            raise Exception("Received unexpected packet")
    except socket.timeout:
        print("Timeout: no response from server")

    # close the socket
    sock.close()


def receive_file(sock, filename):
    with open(filename, 'wb') as file:
        sequence_number = 1
        while True:
            packet, client_address = sock.recvfrom(MAX_PACKET_SIZE)
            seq, ack, flags, win = parse_header(packet)
            syn, ack, fin = parse_flags(flags)
            if fin:
                # FIN packet received, send FIN-ACK packet and exit loop
                ack_packet = create_packet(sequence_number, seq + 1, FIN_FLAG | ACK_FLAG, 0, b'')
                sock.sendto(ack_packet, client_address)
                break
            elif seq == sequence_number:
                # Expected packet received, write data to file and send ACK packet
                data = packet[HEADER_SIZE:]
                file.write(data)
                sequence_number += 1
            ack_packet = create_packet(sequence_number, seq + 1, ACK_FLAG, 0, b'')
            sock.sendto(ack_packet, client_address)
    return file.getvalue()


def main():
    # Parse arguments
    parser = argument_parser()
    args = parser.parse_args()

    # Check if client or server mode is specified
    if not args.client and not args.server:
        print("Error: please specify client (-c) or server (-s) mode.")
        return

    # Create UDP socket and bind to host and port
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((args.host, args.port))

    if args.server:
        # Server mode
        print('Server mode')

        # Receive file from sender
        file_data = receive_file(sock, args.file)
        # TODO: Process received file data

    elif args.client:
        # Client mode
        print('Client mode')

        # Read file data to be sent
        with open(args.file, 'rb') as f:
            file_data = f.read()

        # Send file data to server
        send_file(args.host, args.port, file_data, args.buffer_size, args.timeout)
