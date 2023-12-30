import requests
from account import account_info

username, token, path = account_info()


response = requests.get(   # post to make a new console, get to see live consoles
    f'https://www.pythonanywhere.com/api/v0/user/{username}/consoles/',
    headers={'Authorization': 'Token {token}'.format(token=token)}
)

print('Request Response:')
response_text = response.content.decode('utf-8')
print(response_text)

    



