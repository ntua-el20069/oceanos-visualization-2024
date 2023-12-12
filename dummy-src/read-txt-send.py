import requests

def send_txt_file_to_endpoint(file_path, url, token):
    # Open the .txt file in binary mode to read its content as bytes
    with open(file_path, 'rb') as file:
        txt_content = file.read()

    headers = {
        'Authorization': f'Token {token}',
         'Content-Type': 'text/plain' 
    }

    # Send the .txt file content as data in the POST request
    response = requests.post(url, headers=headers, data=txt_content, verify=False)

    return response

# Define the path to your .txt file
txt_file_path = 'simple.txt'

username = 'oceanosntua'
token = '51fd77231533ea67015675cf29889434f24a391d'
path = f'/home/{username}/oceanos-visualization-2024/demo/csv/out-check.txt'
url = f'https://www.pythonanywhere.com/api/v0/user/{username}/files/path{path}'
## url = 'https://www.pythonanywhere.com/api/v0/user/{username}/cpu/'.format(username=username)


# Send the .txt file to the endpoint
result = send_txt_file_to_endpoint(txt_file_path, url, token)

# Check the response from the server
if result.status_code == 200:
    print("File successfully sent to PythonAnywhere")
else:
    print(f"Failed to send file. Status code: {result.status_code}, Response: {result.text}")
