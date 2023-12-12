import requests

# Replace these with your actual details
file_path = './demo/csv/data2023.csv'
endpoint_url = 'https://oceanos-visualization-demo.netlify.app'

# Open the CSV file and send it via POST request
with open(file_path, 'rb') as file:
    files = {'file': file}
    response = requests.post(endpoint_url, files=files)

print(response.text)
