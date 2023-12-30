import requests
#import json
from account import account_info

username, token, path = account_info()

response = requests.get(
    f'https://www.pythonanywhere.com/api/v0/user/{username}/files/path{path}',
    headers={'Authorization': 'Token {token}'.format(token=token)}
)
if response.status_code == 200:
    print('Request Response:')
    response_text = response.content.decode('utf-8')
    last_line = response_text.split('\n')[-2]
    print(last_line)
    #response_json = json.loads(response.content)
    #print(response_json)
    print("\n\n")
    #for key, value in response_json.items():
        #print(f'{key} : {value}')

else:
    print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))
                        