from threading import Thread
import socket
from helpers.readCSV import readCSV
import time
from requestsAPI.send import send_website
from useful import *



def send_messages(server_socket):
    while True:
        # 8ewroume mia ka8ysterhsh, an den mas aresei thn allazoyme
        if not send_to_host:
            time.sleep(delay)        
        data_now = readCSV(csv_url, fieldnames, realTime = False, delay = delay)
        #before = time.time()
        if send_to_host:
            send_website(data_now, host_write_csv_path, username, token, console_id)
        #print(data_now)
        #after = time.time()
        #print(f'{blue}Pseudo Time: {(after - before):.3f} seconds {reset_color})')

        message = str(data_now)

        if send_to_server:
            #stelnoyme to mnm ston server
            start = time.time()
            try:
                server_socket.sendall(message.encode())
                end = time.time()
                print(f'Send message to server via {blue} TCP {reset_color}(Time consumed: {blue} {(end-start):.3f} seconds {reset_color})')
            except Exception as e:
                print(e)
                print("\n\n\n Calling main from the program... \n\n\n")
                main()
            

        


def main():
    # Connect to the server using the TCP tunnel URL
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    if send_to_server:
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
            print(e)

    # Execute send_messages in main program
    send_messages(server_socket)

if __name__ == '__main__':
    main()