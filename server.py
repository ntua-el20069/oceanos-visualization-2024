import csv
import socket
import threading
import time
from useful import *
from helpers.readCSV import readCSV, MEBC_data_from_total
from helpers.sendWEB import send_website

webhost_response = 'Not sent to web host yet. No Response.'
MEBC_API_response = 'Not sent to MEBC API yet. No Response.'
# Set up Ngrok tunnel
public_url = "oceanos.ngrok.app"
print("Ngrok Tunnel: " + public_url)

def relax(start):
    time_consumed = time.time() - start
    if time_consumed < delay: # if sending was so fast, delay a little (for the remaining time of the delay)
        time.sleep(delay - time_consumed) 

    #print(f'{magenta} Total time {reset_color} for send to HOST & client & sleep: {magenta}  {(time.time() - start):.3f} seconds {reset_color})\n')

def send_messages_web():
    global webhost_response
    while True:
        initial_start = time.time()
        data_now = readCSV(csv_url, fieldnames, realTime = REAL_TIME, delay = delay)
        webhost_response = send_website(data_now)
        print(webhost_response, end='')
        relax(initial_start)

def send_MEBC_API():    ## NOT functional yet
    global MEBC_API_response
    global MEBC_API_url
    global team_token
    while True:
        initial_start = time.time()
        data_now = readCSV(csv_url, fieldnames, realTime = REAL_TIME, delay = delay) ## I should CHANGE something here about fieldnames
        MEBC_API_response = send_website(MEBC_data_from_total(data_now, team_token), MEBC_API_url)
        print(MEBC_API_response, end='')
        relax(initial_start)

# Function to send the last line of the CSV file every second
def send_updates(client_socket):
    global webhost_response
    try:
        # Prepei na stal8ei ena mhnyma apo ton server gia na mporei meta na dextei mhnymata toy client giati exoume krathsei thn epikoinwnia 2 way (h apla prepei na eimaste eygenikoi symfwna me ton skoun)
        client_socket.sendall("Welcome to the chat room!\n".encode())
        while True:
            initial_start = time.time()
            data_now = readCSV(csv_url, fieldnames, realTime = REAL_TIME, delay = delay)
            data_message = str(data_now)
            start = time.time() 
            message = data_message + data_response_delimiter + webhost_response + MEBC_API_response
            client_socket.sendall(message.encode())
            end = time.time()
            print(f'Send message to client via {blue} TCP {reset_color}(Time consumed: {blue} {(end-start):.3f} seconds {reset_color})')
            relax(initial_start)


    except BrokenPipeError as e:
        print(f"Client disconnected: {red}{e}{reset_color}")
    finally:
        client_socket.close()

# Main server function
def start_server():
    
    if send_to_host:
        web_sending = threading.Thread(target=send_messages_web, args= ())
        web_sending.start()
    
    if send_to_MEBC_API:
        MEBC_API_sending = threading.Thread(target=send_MEBC_API, args= ())
        MEBC_API_sending.start()

    if not send_to_client: return

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # avoid bind() exception: OSError: [Errno 98] Address already in use
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind(('localhost', 8080))
    server.listen()

    print("Server listening on {}".format(public_url))

    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr}")
        client_handler = threading.Thread(target=send_updates, args=(client_socket,))
        client_handler.start()

# Run the server
start_server()
