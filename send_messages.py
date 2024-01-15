import socket
from helpers.readCSV import readCSV
import time
from helpers.sendWEB import send_website
from useful import *

def NGROK_connect(server_socket):
    try:
        server_socket.connect(('8.tcp.eu.ngrok.io', 20375))
        # Receive the welcome message from the server
        data = server_socket.recv(1024)
        print(data.decode())
        print("Connected to the server.")
        # Start separate threads for sending and receiving messages
        #send_thread = Thread(target=send_messages, args=(server_socket,))
        #send_thread.start()
    except Exception as e:
        print(f'{red}{e}{reset_color}')

def send_messages(server_socket):
    while True:
        total_start = time.time()
               
        data_now = readCSV(csv_url, fieldnames, realTime = False, delay = delay)

        if send_to_host:
            send_website(data_now)

        message = str(data_now)

        if send_to_server:
            #stelnoyme to mnm ston server
            start = time.time()
            try:
                server_socket.sendall(message.encode())
                end = time.time()
                print(f'Send message to server via {blue} TCP {reset_color}(Time consumed: {blue} {(end-start):.3f} seconds {reset_color})')
            except Exception as e:
                print(f'{red}{e}{reset_color}')
                print("\n\n Trying to connect to server via NGROK again... \n\n")
                NGROK_connect(server_socket)
        total_end = time.time()
        if total_end - total_start < delay: # if sending was so fast, delay a little (for the remaining time of the delay)
            time.sleep(delay - (total_end - total_start)) 
        print(f'{magenta} Total time {reset_color} for send to HOST & server & sleep: {magenta}  {(time.time() - total_start):.3f} seconds {reset_color})\n')

            
if __name__ == '__main__':
    # Connect to the server using the TCP tunnel URL
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    if send_to_server:
        NGROK_connect(server_socket)

    # Execute send_messages in main program
    send_messages(server_socket)


