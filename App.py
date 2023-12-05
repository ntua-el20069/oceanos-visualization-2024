
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, Oceanos NTUA!'

if __name__ == '__main__':
    app.run(debug=True)



'''
import requests
username = 'oceanosntua'
token = '51fd77231533ea67015675cf29889434f24a391d'

response = requests.get(
    'https://www.pythonanywhere.com/api/v0/user/{username}/cpu/'.format(
        username=username
    ),
    headers={'Authorization': 'Token {token}'.format(token=token)}
)
if response.status_code == 200:
    print('CPU quota info:')
    print(response.content)
else:
    print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))
                        

########

import csv
import requests

# Replace with your actual PythonAnywhere API token
API_TOKEN = 'your_api_token'
API_URL = 'https://www.pythonanywhere.com/api/v0/user/{username}/files/path/{path}'  # Replace with the appropriate API endpoint

# Function to read the last line of the CSV file
def read_last_line_of_csv(file_name):
    with open(file_name, 'r') as file:
        last_line = file.readlines()[-1]
    return last_line

# Function to send data to PythonAnywhere using API
def send_data_to_pythonanywhere(api_token, data, api_url):
    headers = {
        'Authorization': f'Token {api_token}'
    }
    response = requests.post(api_url, headers=headers, data=data)
    if response.status_code == 200:
        print("Data successfully sent to PythonAnywhere")
    else:
        print(f"Failed to send data. Status code: {response.status_code}, Response: {response.text}")

# Main execution
if __name__ == "__main__":
    csv_file = 'demo/csv/data2023.csv'  # Name of your CSV file
    last_line = read_last_line_of_csv(csv_file)
    send_data_to_pythonanywhere(API_TOKEN, last_line, API_URL)
'''