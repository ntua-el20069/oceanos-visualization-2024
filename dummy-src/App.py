
from flask import Flask, render_template
import requests
import csv


username = 'oceanosntua'
token = '51fd77231533ea67015675cf29889434f24a391d'


#API_URL = f'https://www.pythonanywhere.com/api/v0/user/{username}/files/path/{path}'  # Replace with the appropriate API endpoint
url = f'https://www.pythonanywhere.com/api/v0/user/{username}/cpu/'

########

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
    response = requests.post(api_url, headers=headers, data=data, verify=False)
    if response.status_code == 200:
        return "Data successfully sent to PythonAnywhere"
    else:
        return f"Failed to send data. Status code: {response.status_code}, Response: {response.text}"


app = Flask(__name__)

@app.route('/')
def index():
    
    csv_file = 'demo/csv/data2023.csv'  # Name of your CSV file
    last_line = read_last_line_of_csv(csv_file)
    send_data_to_pythonanywhere(token, last_line, url)

    response = requests.get(
        url,
        headers={'Authorization': 'Token {token}'.format(token=token)},
        verify=False
    )
    if response.status_code == 200:
        return 'CPU quota info:' + f'<br> response content = {response.content}' + '<br>'
        #print(response.content)
    else:
        return 'Got unexpected status code {}: {!r}'.format(response.status_code, response.content) + '<br>'
                       
    return 'Hello, Oceanos NTUA!'

app.route('/demo')
def telemetry_demo():
    render_template('')

if __name__ == '__main__':
    app.run(debug=True)

         


'''# Main execution
if __name__ == "__main__":
    csv_file = 'demo/csv/data2023.csv'  # Name of your CSV file
    last_line = read_last_line_of_csv(csv_file)
    send_data_to_pythonanywhere(token, last_line, API_URL)'''
