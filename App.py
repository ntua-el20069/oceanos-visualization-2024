
from flask import Flask, render_template, redirect, url_for, jsonify
from threading import Thread
import socket
import random
import time
import pandas as pd
import numpy as np
import asyncio
from requestsAPI.send import send_website
from requestsAPI.readline import readline

mode = 'local' # mode is 'local' or 'web' depending on if we want to run the script in our local computer or in pythonanywhere

app = Flask(__name__)

data_now = {}  # Global variable to store the data we want to send to server and visualize

fieldnames =["current_time", "latitude", "longitude", "speed", "miles", "miles_lap", "rtc", "millis", "rpm", "input_voltage", "motor_watt", "motor_tempMosfet", "motor_tempMotor", "motor_current", "battery_current","motor_dutyCycle", "motor_error", "rasp_temp", "battery_ampere", "battery_voltage", "charge", "battery_temperature", "autonomy"]

csv_url = 'static/csv/serverdata_2023-12-17_16-11-34.csv'  ### CHANGE with the path of the CSV you want to visualize Live (Normal Mode)

host_write_csv_path = 'hostdata.csv'
host_read_csv_path = f'/home/oceanosntua/oceanos-visualization-2024/static/csv/{host_write_csv_path}'

def send_messages(server_socket):
    global data_now
    counter = 10
    while True:
        # 8ewroume mia ka8ysterhsh, an den mas aresei thn allazoyme
        time.sleep(0.5)        # CHANGE (delay of taking data from CSV)
        data = pd.read_csv(csv_url, delimiter=',')  # diabazw to arxeio
        ######## Random Index for Demo
        counter = ( counter + 1 ) % len(data) #random.randint(start, end)
        
        #print(f"\nIndex is: ########################      ######################  {counter}\n")
        # ftiaxnw dianysma me tis times apo thn teleytaia seira tou arxeiou
        data1 = np.array(data.iloc[counter].values)    #### CHANGE !!!!! counter to -1 for real time last data

        #print(str(data1.size)+"---------------------------------------------------")
        # bazw se ka8e metablhth thn antistoixh timh apo to panw dianusma se morfh str gia na emfanizetai sthn o8onh swsta
        ### Update global data_now
        data_now = {label : str(x) for label, x in zip(fieldnames, data1)}        

        asyncio.run(send_website(data_now, host_write_csv_path))
        #print(data_now)

        message = str(data_now)
        
        #stelnoyme to mnm ston server
        server_socket.sendall(message.encode())
        
        
@app.route('/')  # basic web route
def home():
    return render_template('telemetry.html') 

@app.route('/reload') # reload data, update visualization (a JavaScript function fetches this JSON data every 1 sec)
def reload():  
    global data_now
    if mode == 'local':
        return jsonify(data_now)
    else: # 'web' mode
        return jsonify(readline(host_read_csv_path, fieldnames))  

@app.route('/example') # example about how fetch & reload works
def example():
    return render_template('example.html')

@app.route('/roundSlider') # roundSlider demo for different types of circular inputs
def roundSlider():
    return render_template('demo.html')

def visualization():
    app.run(host='0.0.0.0', use_reloader=False, debug=True)

if __name__ == '__main__':

    # Connect to the server using the TCP tunnel URL
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    server_socket.connect(('8.tcp.eu.ngrok.io', 20375))
    # Receive the welcome message from the server
    data = server_socket.recv(1024)
    print(data.decode())
    print("Connected to the server.")
    # Start separate threads for sending and receiving messages
    #send_thread = Thread(target=send_messages, args=(server_socket,))
    #send_thread.start()
    
    # Start separate thread for visualization
    web_thread = Thread(target=visualization, args=())
    web_thread.start()

    # Execute send_messages in main program
    send_messages(server_socket)
    
    

