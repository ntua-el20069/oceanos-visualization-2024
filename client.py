import socket
import csv
import time

# Connect to the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('8.tcp.eu.ngrok.io', 20375))  # Replace YOUR_NGROK_PORT with the port provided by ngrok
#previous = time.time()
# Test gia na fanei oti leitoyrgei h syndesh
fieldnames =["current_time", "latitude", "longitude", "speed", "miles", "miles_lap", "rtc", "millis", "rpm", "input_voltage", "motor_watt", "motor_tempMosfet", "motor_tempMotor", "motor_current", "battery_current","motor_dutyCycle", "motor_error", "rasp_temp", "battery_ampere", "battery_voltage", "charge", "battery_temperature", "autonomy"]
print(fieldnames)
# Receive the welcome message from the server
data = client.recv(1024)
print(f"\n\n\t {data.decode()}")
print("\n\n\t Connected to the server.\n\n")

#writing sto csv in append mode
with open('serverdata.csv', 'a') as csv_file:
	csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
	csv_writer.writeheader()

try:
    while True:
        # Receive data from the server
        response = client.recv(4096)
        if not response:
            break
        print(response.decode())
        print()
        #print(f'Total time to respond:  {(time.time() - previous):.3f} seconds)\n')
        #previous = time.time()
        #print()
finally:
    client.close()
