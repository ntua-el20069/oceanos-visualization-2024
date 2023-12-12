import requests
username = 'oceanosntua'
token = '51fd77231533ea67015675cf29889434f24a391d'
path = f'/home/{username}/oceanos-visualization-2024/demo/csv/data2023.csv'
url = f'https://www.pythonanywhere.com/api/v0/user/{username}/files/path{path}'
## url = 'https://www.pythonanywhere.com/api/v0/user/{username}/cpu/'.format(username=username)
response = requests.get(
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
              