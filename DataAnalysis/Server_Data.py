import requests
#import json
from Account import account_info
import pandas as pd
from io import StringIO

username, token = account_info()

repo = 'oceanos-visualization-2024'
path = f'/home/{username}/hostdata.csv'

fieldnames =["current_time", "latitude", "longitude", "speed", "miles", "miles_lap", "rtc", "millis", "rpm", "input_voltage", "motor_watt", "motor_tempMosfet", "motor_tempMotor", "motor_current", "battery_current","motor_dutyCycle", "motor_error", "rasp_temp", "battery_ampere", "battery_voltage", "charge", "battery_temperature", "autonomy"]

response = requests.get(
    f'https://www.pythonanywhere.com/api/v0/user/{username}/files/path{path}',
    headers={'Authorization': 'Token {token}'.format(token=token)}
)
if response.status_code == 200:
    text = response.content
    response_text = response.content.decode('utf-8')
        # Use StringIO to create a file-like object from the string
    csv_data = StringIO(response_text)

    # Use pd.read_csv to read the CSV data into a DataFrame
    data = pd.read_csv(csv_data)