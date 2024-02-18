import socket
import csv
import time
import json
from useful import *
from datetime import datetime
import os

dir = os.getcwd()

# rename the serverdata and save it to another folder (history)
try:
    old_fn = client_read_csv_path
    new_fn = 'clientdata_' + datetime.today().strftime("%Y-%m-%d") + '_' + datetime.now().strftime("%H-%M-%S") + '.csv'

    # Use os.path.join for proper path construction
    os.rename(os.path.join(dir, old_fn), os.path.join(dir + "/csv history/", new_fn))
except Exception as e:
    print(e)

# Connect to the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('8.tcp.eu.ngrok.io', 20628))  # Replace YOUR_NGROK_PORT with the port provided by ngrok
#previous = time.time()
# Test gia na fanei oti leitoyrgei h syndesh
print(fieldnames)
# Receive the welcome message from the server
data = client.recv(4096)
print(f"\n\n\t {data.decode()}")
print("\n\n\t Connected to the server.\n\n")

#writing sto csv in append mode
with open(client_read_csv_path, 'a') as csv_file:
	csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
	csv_writer.writeheader()

try:
    while True:
        # Receive data from the server
        response = client.recv(4096)
        if not response:
            print(f"\n\t Received empty data (maybe server closed) \n")
            break
        data, webhost_response =  response.decode('utf-8').split(data_response_delimiter)
        my_str = data.replace("'", '"')

        ## when the data sending stops, we receive the empty string as message
        if not my_str: continue  # the empty string cannot be JSON decoded
        data2 = json.loads(my_str)
        
        with open(client_read_csv_path, 'a') as csv_file: #open test1 in append mode, keep appending to the csv
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        #ta dedomena gia ta headers
        #na prosthesw sto data to time
            csv_writer.writerow(data2) #writes one row at a time sto test1.csv
            csv_file.close()

        print(my_str)
        print()
        print(webhost_response)
        #print(f'Total time to respond:  {(time.time() - previous):.3f} seconds)\n')
        #previous = time.time()
        #print()
finally:
    client.close()
    print("\n\t Client closed \n")
