
from flask import Flask, render_template, redirect, url_for, jsonify
from threading import Thread, Lock
import socket
import random
import time
import pandas as pd
import numpy as np

app = Flask(__name__)


## If you want to use Locks Ctrl+F     #LOCK#      and change appropriately the code blocks there

#LOCK#lock = Lock()  # Create a lock object

time_var = ''  # Global variable to store the time value

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/reload')
def reload():
    #LOCK#with lock:    
    global time_var
    print(time_var)
    return jsonify({'time_var': time_var})  


app.route('/demo')
def telemetry_demo():
    render_template('')

def send_messages(server_socket):
    global time_var
    while True:
        # 8ewroume mia ka8ysterhsh, an den mas aresei thn allazoyme
        time.sleep(0.5)
        # diabazw to arxeio
        data = pd.read_csv('demo/csv/data2023.csv', delimiter=';')
        # ftiaxnw dianysma me tis times apo thn teleytaia seira tou arxeiou
        
        ######## Random Index for Demo

        start = 0  # Replace with your desired start index
        end = len(data) - 1  # Replace with your desired end index

        #  random integer between start and end
        random_i = random.randint(start, end)

        #######

        data1 = np.array(data.iloc[random_i].values)    #### CHANGE !!!!! random_i to -1 for real time last data

        #######

        #print(str(data1.size)+"---------------------------------------------------")
        # bazw se ka8e metablhth thn antistoixh timh apo to panw dianusma se morfh str gia na emfanizetai sthn o8onh swsta
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
        message = str({"current_time": current_time,"latitude": lat, "longitude": longt,"speed": speed, "miles": miles, "miles_lap": miles_lap, "rtc": rtc,"millis": millis,"rpm": rpm,"input_voltage": input_voltage,"motor_watt":motor_watt,"motor_tempMosfet": motor_tempMosfet,"motor_tempMotor": motor_tempMotor,"motor_current":motor_current,"battery_current":battery_current,"motor_dutyCycle":motor_dutyCycle,"motor_error":motor_error, "rasp_temp": rasp_temp, "battery_ampere": battery_ampere, "battery_voltage": battery_voltage, "charge": charge, "battery_temperature": battery_temperature})
        #stelnoyme to mnm ston server
        server_socket.sendall(message.encode())
        ### Update global time
        
        #LOCK#with lock:
        time_var = current_time
            
  
if __name__ == '__main__':

    #with app.app_context():
    #    g.time_var = ''

    # Connect to the server using the TCP tunnel URL
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect(('8.tcp.eu.ngrok.io', 20375))
    print("Connected to the server.")

    # Receive the welcome message from the server
    data = server_socket.recv(1024)
    print(data.decode())

    # Start separate threads for sending and receiving messages
    send_thread = Thread(target=send_messages, args=(server_socket,))
    send_thread.start()
    

    ###  Run the Flask app for the web browser
    app.run(debug=True)

         
