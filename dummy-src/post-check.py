import requests
import json

username = 'oceanosntua'
token = '51fd77231533ea67015675cf29889434f24a391d'
path = f'/home/{username}/oceanos-visualization-2024/demo/csv/out-check.txt'
url = f'https://www.pythonanywhere.com/api/v0/user/{username}/files/path{path}'
## url = 'https://www.pythonanywhere.com/api/v0/user/{username}/cpu/'.format(username=username)

# Function to read the last line of the CSV file
def read_last_line_of_csv(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        last_line = lines[-1] if lines else None  # Check if the file is not empty
    return last_line


csv_file = 'demo/csv/data2023.csv'  # Name of your CSV file
last_line = read_last_line_of_csv(csv_file)

headers = {
        'Authorization': f'Token {token}'
    }

#json_data = json.loads(last_line)
response = requests.post(url, headers=headers, data=last_line, verify=False)
if response.status_code == 200:
    print("Data successfully sent to PythonAnywhere")
else:
    print(f"Failed to send data. Status code: {response.status_code}, Response: {response.text}")

'''response = requests.post(
    url,
    headers={'Authorization': 'Token {token}'.format(token=token)},
    verify=False
)
if response.status_code == 200:
    print('CPU quota info:')
    #print(response.content)
    #   response.content type is bytes 
    out = response.content.decode('utf-8')
    print(type(out))
    print(type(out.split('\n')))
    data = out.split('\n')
    print("\n\n")
    for i in range(3):
        print(f"Row Number {i}")
        print(data[i])
        print("\n\n\n")
else:
    print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))
'''              