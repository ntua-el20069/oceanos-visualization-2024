import socket
from helpers.readCSV import readCSV
import time
import timeit
from helpers.sendWEB import send_website
from useful import *

global server_socket

def NGROK_connect() -> socket:
    try:
        # Connect to the server using the TCP tunnel URL
        new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        new_socket.connect(('8.tcp.eu.ngrok.io', 20375))
        # Receive the welcome message from the server
        data = new_socket.recv(1024)
        print(data.decode())
        print("Connected to the server.")
        # Start separate threads for sending and receiving messages
        #send_thread = Thread(target=send_messages, args=(server_socket,))
        #send_thread.start()
    except Exception as e:
        print(f'{red}{e}{reset_color}')
    return new_socket

def send_messages():
    global server_socket
    while True:
        total_start = time.time()
        data_now = readCSV(csv_url, fieldnames, realTime = REAL_TIME, delay = delay)
        message = str(data_now) 

        if send_to_server:
            #stelnoyme to mnm ston server
            start = time.time()
            try:
                server_socket.sendall(message.encode())
                end = time.time()
                print(f'Send message to server via {blue} TCP {reset_color}(Time consumed: {blue} {(end-start):.3f} seconds {reset_color})')
            except Exception as e:
                end = time.time()
                print(f'{red}{e}{reset_color} (Time consumed: {blue}{(end-start):.3f} seconds{reset_color}). Trying to connect to server via NGROK again...', end=' ')
                server_socket = NGROK_connect()

        if send_to_host:
            webhost_response = send_website(data_now)
            print(webhost_response, end='')

        if send_to_server and send_to_host: # Send the Web Host Response to the server to be aware about what happens...
            try:
                server_socket.sendall(webhost_response.encode())
            except Exception as e:
                print(f'{red}{e}{reset_color} Trying to connect to server via NGROK again...', end = ' ')
                server_socket = NGROK_connect()

        total_end = time.time()
        if total_end - total_start < delay: # if sending was so fast, delay a little (for the remaining time of the delay)
            time.sleep(delay - (total_end - total_start)) 
        print(f'{magenta} Total time {reset_color} for send to HOST & server & sleep: {magenta}  {(time.time() - total_start):.3f} seconds {reset_color})\n')

            
if __name__ == '__main__':

    if send_to_server:
        server_socket = NGROK_connect()

    # Execute send_messages in main program
    send_messages()


