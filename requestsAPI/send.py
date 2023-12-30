import requests
import json
import os
from requestsAPI.account import account_info

username, token, path = account_info()
id = 31689948


def send_website(data_now: dict, csv_name: str):
    python_script = f'''
import os
newline_character = os.linesep
separator = ','
data_now = {data_now}
csv_line = separator.join(list(data_now.values())).replace('nan','')
with open('{csv_name}','a',encoding='utf-8') as csvFile:
    csvFile.write(csv_line)
    csvFile.write(newline_character)
'''
    console_log = {'input' : f'python\n{python_script}\nexit()\n'}

    response = requests.post(
        f'https://www.pythonanywhere.com/api/v0/user/{username}/consoles/{id}/send_input/',
        headers={'Authorization': f'Token {token}'},
        json=console_log   
    )

    print('Request Response:')
    response_text = response.content.decode('utf-8')
    print(response_text)
    