import socket
from threading import Thread
#from pyngrok import ngrok
import csv
from datetime import datetime
import ast
import pandas as pd
import json
import os

dir = "/Users/vassdel/Library/CloudStorage/OneDrive-ΕθνικόΜετσόβιοΠολυτεχνείο/Oceanos/Arduino/vesc_can_bus_arduino"

# rename the serverdata and save it to another folder (history)
try:
    old_fn = 'serverdata.csv'
    new_fn = 'serverdata_' + datetime.today().strftime("%Y-%m-%d") + '_' + datetime.now().strftime("%H-%M-%S") + '.csv'

    # Use os.path.join for proper path construction
    os.rename(os.path.join(dir, old_fn), os.path.join(dir + "/server history/", new_fn))
except:
    pass

'''Για να τρέξουμε αρχικά τον σερβερ, τρεχουμε το αρχειο ngrok.exe και του δινουμε την εντολη ngrok tcp 8080 or ngrok tcp --region=eu --remote-addr=3.tcp.eu.ngrok.io:28669 8080
Μετα βλεπουμε το Forwarding και αλλαζουμε στο αρχειο ngrok_TRANSMIT καταλληλα την εντολη server_socket.connect(('---.tcp.eu.ngrok.io',-----))
(^Αυτο είναι γιατι εχω φρι λαισενς αλλιως ειναι σταθερά και δεν εχουμε θέμα)
Μετα τρέχουμε το Final_server.py και τον ngrok_TRANSMIT.py τρέχει στο ρασμπερι
Για να δουμε το visualisation τρεχουμε το main1.py'''

def send_messages(client_socket):
    while True:
        # Get a message from the user and send it to the client
        message = input("")
        client_socket.sendall(message.encode())

def receive_messages(client_socket):
    while True:
        # Receive a message from the client and print it
        # print("hello")
        data = client_socket.recv(1024)
        my_str = data.decode('utf-8').replace("'", '"')
        #print(len(my_str))
        #my_str2=my_str.replace(" ",'"')
        if 'Response' in my_str:  # handle response message about webhost message sending
            print(my_str)
            continue
        if len(my_str)<=600:
            if len(my_str)>=150:
                data2 = json.loads(my_str)
                with open('serverdata.csv', 'a') as csv_file: #open test1 in append mode, keep appending to the csv
                    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                #ta dedomena gia ta headers
                #na prosthesw sto data to time
                    csv_writer.writerow(data2) #writes one row at a time sto test1.csv
                    csv_file.close()
                if not data:
                    break
                print(f"{data.decode()}")

# Set up the socket to listen for incoming connections
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8080))
server_socket.listen(1)
# Test gia na fanei oti leitoyrgei h syndesh
fieldnames =["current_time", "latitude", "longitude", "speed", "miles", "miles_lap", "rtc", "millis", "rpm", "input_voltage", "motor_watt", "motor_tempMosfet", "motor_tempMotor", "motor_current", "battery_current","motor_dutyCycle", "motor_error", "rasp_temp", "battery_ampere", "battery_voltage", "charge", "battery_temperature", "autonomy"]
print(fieldnames)

#writing sto csv in append mode
with open('serverdata.csv', 'a') as csv_file:
	csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
	csv_writer.writeheader()


# Accept incoming connections and start receiving data
while True:
    client_socket, addr = server_socket.accept()
    print(f"Connected by {addr}")
    # Prepei na stal8ei ena mhnyma apo ton server gia na mporei meta na dextei mhnymata toy client giati exoume krathsei thn epikoinwnia 2 way (h apla prepei na eimaste eygenikoi symfwna me ton skoun)
    client_socket.sendall("Welcome to the chat room!\n".encode())

    # Start separate threads for sending and receiving messages
    send_thread = Thread(target=send_messages, args=(client_socket,))
    recv_thread = Thread(target=receive_messages, args=(client_socket,))
    send_thread.start()
    recv_thread.start()