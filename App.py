
from flask import Flask, render_template, redirect, url_for, jsonify
from threading import Thread
import socket
import random
import time
import pandas as pd
import numpy as np
from requestsAPI.send import send_website
from requestsAPI.readline import readline

mode = 'local' # mode is 'local' or 'web' depending on if we want to run the script in our local computer or in pythonanywhere

app = Flask(__name__)

data_now = {}  # Global variable to store the data we want to send to server and visualize

fieldnames =["current_time", "latitude", "longitude", "speed", "miles", "miles_lap", "rtc", "millis", "rpm", "input_voltage", "motor_watt", "motor_tempMosfet", "motor_tempMotor", "motor_current", "battery_current","motor_dutyCycle", "motor_error", "rasp_temp", "battery_ampere", "battery_voltage", "charge", "battery_temperature", "autonomy"]

csv_url = 'static/csv/serverdata_2023-12-17_16-11-34.csv'  ### CHANGE with the path of the CSV you want to visualize Live (Normal Mode)

host_write_csv_path = 'hostdata.csv'
host_read_csv_path = 'static/csv/hostdata.csv'

def send_messages(server_socket):
    global data_now
    counter = 10
    while True:
        # 8ewroume mia ka8ysterhsh, an den mas aresei thn allazoyme
        time.sleep(0.5)        # CHANGE (delay of taking data from CSV)
        # diabazw to arxeio
        
        
        data = pd.read_csv(csv_url, delimiter=',')
        # ftiaxnw dianysma me tis times apo thn teleytaia seira tou arxeiou
        
        ######## Random Index for Demo
        counter = ( counter + 1 ) % len(data) #random.randint(start, end)
        random_i = counter
        #######

        data1 = np.array(data.iloc[random_i].values)    #### CHANGE !!!!! random_i to -1 for real time last data
        
        #######

        #print(str(data1.size)+"---------------------------------------------------")
        # bazw se ka8e metablhth thn antistoixh timh apo to panw dianusma se morfh str gia na emfanizetai sthn o8onh swsta
        ''' # bad code ...
        current_time = str(data1[0])
        lat = str(data1[1])
        longt = str(data1[2])
        speed = str(data1[3])
        miles = str(data1[4])
        miles_lap = str(data1[5])
        rtc = str(data1[6])
        millis = str(data1[7])
        rpm = str(data1[8])
        input_voltage = str(data1[9])
        motor_watt = str(data1[10])
        motor_tempMosfet = str(data1[11])
        motor_tempMotor = str(data1[12])
        motor_current = str(data1[13])
        battery_current = str(data1[14])
        motor_dutyCycle = str(data1[15])
        motor_error = str(data1[16])
        rasp_temp = str(data1[17])
        battery_ampere = str(data1[18])
        battery_voltage = str(data1[19])
        charge = str(data1[20])
        battery_temperature = str(data1[21])
        
        ### Update global data_now
        data_now = {"current_time": current_time,"latitude": lat, "longitude": longt,"speed": speed, "miles": miles, "miles_lap": miles_lap, "rtc": rtc,"millis": millis,"rpm": rpm,"input_voltage": input_voltage,"motor_watt":motor_watt,"motor_tempMosfet": motor_tempMosfet,"motor_tempMotor": motor_tempMotor,"motor_current":motor_current,"battery_current":battery_current,"motor_dutyCycle":motor_dutyCycle,"motor_error":motor_error, "rasp_temp": rasp_temp, "battery_ampere": battery_ampere, "battery_voltage": battery_voltage, "charge": charge, "battery_temperature": battery_temperature}

        '''
        
         ### Update global data_now
        data_now = {label : str(x) for label, x in zip(fieldnames, data1)}        
       
        send_website(data_now, host_write_csv_path)

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

if __name__ == '__main__':

    # Connect to the server using the TCP tunnel URL
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    server_socket.connect(('8.tcp.eu.ngrok.io', 20375))
    # Receive the welcome message from the server
    data = server_socket.recv(1024)
    print(data.decode())

    # Start separate threads for sending and receiving messages
    send_thread = Thread(target=send_messages, args=(server_socket,))
    send_thread.start()
    print("Connected to the server.")

    ###  Run the Flask app for the web browser
    app.run(debug=True)

         
