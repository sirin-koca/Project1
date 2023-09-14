# DATA2410 - Network and Cloud Computing - Portfolio1 - s182211
"""In this project, I will design and implement a simplified version of iperf using sockets, called simpleperf. The
simpleperf tool will be used to measure the performance of a virtual network managed by Mininet inside a virtual
machine. The simpleperf tool will have two modes: server mode and client mode. In server mode, it will receive TCP
packets and track the amount of data received. In client mode, it will establish a TCP connection with the server and
send data. The main objectives of the project are to implement simpleperf, run it in both modes, and evaluate its
performance using Mininet."""

import socket
import time
import threading
from argparse import ArgumentParser

# Default values
DEFAULT_IP = '0.0.0.0'
DEFAULT_PORT = 8088
DEFAULT_FORMAT = 'MB'


def parse_arguments():
    # Setup command line arguments
    parser = ArgumentParser(description='Simpleperf')
    parser.add_argument('-s', '--server', action='store_true', help='enable server mode')
    parser.add_argument('-b', '--bind', default='0.0.0.0', help='server IP address to bind to')
    parser.add_argument('-p', '--port', default=8088, type=int, help='server port to listen on')
    parser.add_argument('-f', '--format', default='MB', choices=['B', 'KB', 'MB'], help='output format')
    parser.add_argument('-c', '--client', action='store_true', help='run in client mode')
    parser.add_argument('-I', '--serverip', type=str, help='IP address of the server')
    parser.add_argument('-t', '--time', type=int, default=25, help='duration in seconds')
    parser.add_argument('-i', '--interval', type=int, default=None, help='interval to print statistics')
    parser.add_argument('-P', '--parallel', type=int, default=1, help='number of parallel connections to create')
    parser.add_argument('-n', '--num', type=str, help='number of bytes to transfer')
    args = parser.parse_args()
    return args


# Print data transfer statistics at the specified interval.
def print_interval_stats(start_time, bytes_transferred, data_format, interval):
    elapsed_time = time.time() - start_time
    transferred = bytes_transferred / (1000 ** (1 if data_format == "KB" else 2))
    rate = bytes_transferred * 8 / elapsed_time / 1000000
    print(f"Interval: {elapsed_time:.2f} s | Transferred: {transferred:.2f} {data_format} | Rate: {rate:.2f} Mbps")


# In server mode, it will receive TCP packets and track the amount of data received.
def server(args):
    try:
        # Creating socket object:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the socket to the IP address and port-number:
        server_socket.bind((args.bind, args.port))

        # Server is listening for incoming connections:
        server_socket.listen(args.parallel)

        print(f'A simpleperf server is listening on port {args.port}')

        while True:
            # Server will wait for a client to connect
            client_socket, client_address = server_socket.accept()

            print(
                f'A simpleperf client with {client_address[0]}:{client_address[1]} is connected with {args.bind}:{args.port}')

            # Wrap the connection handling in a try-except block
            try:
                start_time = time.time()
                total_bytes = 0
                last_report_time = start_time

                while True:
                    # Server receive 1000 bytes of data from the client
                    data = client_socket.recv(1000)
                    if not data:
                        break

                    total_bytes += len(data)

                    current_time = time.time()
                    if args.interval is not None and current_time - last_report_time >= args.interval:
                        print_interval_stats(last_report_time, total_bytes, args.format, args.interval)
                        last_report_time = current_time
                        total_bytes = 0

                    # Break the loop when the specified number of bytes is reached
                    if args.num is not None and total_bytes >= int(args.num):
                        break

                elapsed_time = time.time() - start_time

                if elapsed_time >= args.time or (args.num is not None and total_bytes >= int(args.num)):
                    # Send a confirmation message to the client
                    client_socket.send(b'ACK: END')

                    # Calculate and print the result
                    transferred = total_bytes / (1000 ** (1 if args.format == "KB" else 2))
                    rate = total_bytes * 8 / elapsed_time / 1000000
                    print(
                        f"ID: {client_address[0]}:{client_address[1]} | Interval: {elapsed_time:.2f} s | Received: {transferred:.0f} {args.format} | Rate: {rate:.2f} Mbps")
                    break

            except Exception as e:
                print(f"Error occurred during connection handling: {e}")
            finally:
                # Close the connection with the client
                client_socket.close()

    except Exception as e:
        print(f"Error occurred in server: {e}")


# In client mode, it will establish a TCP connection with the server and send data.
def single_connection(args):
    client_socket = None

    try:
        # Check if the server IP and port are specified
        if args.serverip is None or args.port is None:
            print("Error: you must specify the server IP and port")
            return
        else:
            server_address = (args.serverip, args.port)

        # Create a client socket and connect to the server
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(server_address)

        # Send start message to server
        client_socket.sendall(b'START')

        # Initialize statistics variables
        stats = {
            'bytes_sent': 0,
            'start_time': time.time(),
            'last_report_time': time.time(),
            'current_time': time.time()
        }

        # Send data to the server until the specified number of bytes is reached or time limit is exceeded
        while (args.num is None or stats['bytes_sent'] < int(args.num)) and (args.time is None or stats['current_time'] - stats['start_time'] < args.time):
            data = bytearray(1000)
            client_socket.sendall(data)
            stats['bytes_sent'] += len(data)
            stats['current_time'] = time.time()

            # Print interval statistics if specified interval has elapsed
            if args.interval is not None and stats['current_time'] - stats['last_report_time'] >= args.interval:
                print_interval_stats(stats['last_report_time'], stats['bytes_sent'], args.format, args.interval)
                stats['last_report_time'] = stats['current_time']
                stats['bytes_sent'] = 0

            # Break the loop when the specified number of bytes is reached
            if args.num is not None and stats['bytes_sent'] >= int(args.num):
                break

            # Break the loop when the time limit is exceeded
            elapsed_time = stats['current_time'] - stats['start_time']
            if elapsed_time >= args.time:
                break

        # Send END message to the server
        client_socket.sendall(b'END')

        # Wait for acknowledgement message from the server
        ack = client_socket.recv(1024)
        if ack != b'ACK: END':
            print("Error: failed to receive acknowledgement from server")

    except Exception as e:
        print(f"Error occurred in single_connection: {e}")
        import traceback
        traceback.print_exc()
    finally:
        # Send BYE message to the server and close the client socket
        if client_socket is not None:
            client_socket.sendall(b'BYE')
            client_socket.close()


# Creating multiple threads to run parallel connections to the server in the client function.
def client(args):
    threads = []
    for i in range(args.parallel):
        t = threading.Thread(target=single_connection, args=(args,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


def main():
    args = parse_arguments()
    if args.server:
        server(args)
    elif args.client:
        client(args)
    else:
        print("Error: you must run either in server or client mode")


if __name__ == '__main__':
    main()