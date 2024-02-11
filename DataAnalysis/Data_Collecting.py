import pandas as pd
import numpy as np
import time
import csv

# this program starts running in the beginning of the test
fieldnames =["current_time", "latitude", "longitude", "speed", "miles", "miles_lap", "rtc", "millis", "rpm", "input_voltage", "motor_watt", "motor_tempMosfet", "motor_tempMotor", "motor_current", "battery_current","motor_dutyCycle", "motor_error", "rasp_temp", "battery_ampere", "battery_voltage", "charge", "battery_temperature", "autonomy"]

data_now = {}  # Global variable to store the data we want to send to server and visualize

def get_messages():
    global data_now
    counter = 10
    
    while True:
        # 8ewroume mia ka8ysterhsh, an den mas aresei thn allazoyme
        time.sleep(0.5)        # CHANGE (delay of taking data from CSV)
        csv_url = 'received_data/serverdata_2023-12-17_16-11-34.csv'  ### this should change with the actual path
        # if we do it on https://oceanosntua.pythonanywhere.com/ this step can be skipped.
        data = pd.read_csv(csv_url, delimiter=',')

        ######## Random Index for Demo
        counter = ( counter + 1 ) % len(data) #random.randint(start, end)
        random_i = counter

        data1 = np.array(data.iloc[random_i].values)    #### CHANGE !!!!! random_i to -1 for real time last data

        with open('created_data/data.csv', 'a') as csv_file: #open test1 in append mode, keep appending to the csv

            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            ### Update global data_now
            data_now = {label : str(x) for label, x in zip(fieldnames, data1)}
            csv_writer.writerow(data_now)
            csv_file.close()

if __name__ == '__main__':

    get_messages()