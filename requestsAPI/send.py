import requests
import json
import os
from requestsAPI.account import account_info
import aiohttp

username, token, path = account_info()
id = 31692730


async def send_website(data_now: dict, csv_name: str):
    separator = ','
    csv_line = separator.join(list(data_now.values())).replace('nan','')
    python_script = f'''
with open('{csv_name}','a',encoding='utf-8') as csvFile:
    print("{csv_line}", file=csvFile)         
'''
    bash_script = f'''echo "{csv_line}" >> "{csv_name}" '''
    #console_log = {'input' : f'python\n{python_script}\nexit()\n'}
    console_log = {'input' : f'{bash_script}\n'}

    async with aiohttp.ClientSession() as session:
        response = requests.post(
            f'https://www.pythonanywhere.com/api/v0/user/{username}/consoles/{id}/send_input/',
            headers={'Authorization': f'Token {token}'},
            json=console_log   
        )

        print('Request Response:')
        response_text = response.content.decode('utf-8')
        print(response_text)
    