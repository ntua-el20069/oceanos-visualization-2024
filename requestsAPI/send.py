import requests
import time

green = "\033[32m"
red = "\033[31m"
# Reset ANSI escape code for default text color
reset_color = "\033[0m"

def send_website(data_now: dict, csv_name: str, username, token, id):
    separator = ','
    csv_line = separator.join(list(data_now.values())).replace('nan','')
    python_script = f'''
with open('{csv_name}','a',encoding='utf-8') as csvFile:
    print("{csv_line}", file=csvFile)         
'''
    bash_script = f'''echo "{csv_line}" >> "{csv_name}" '''
    #console_log = {'input' : f'python\n{python_script}\nexit()\n'}
    console_log = {'input' : f'{bash_script}\n'}

    start = time.time()

    try: 
        response = requests.post(
        f'https://www.pythonanywhere.com/api/v0/user/{username}/consoles/{id}/send_input/',
        headers={'Authorization': f'Token {token}'},
        json=console_log ,
        timeout=1
        )
        response.raise_for_status() 
        end = time.time()

        response_text = response.content.decode('utf-8')
        
        print(f'{green} HTTP POST {reset_color} Request Response: (Time consumed: {green} {(end-start):.3f} seconds {reset_color})')
        print(f"{green}{response_text}{reset_color}")
    
    except requests.exceptions.ConnectTimeout as err:
        print(f"{red}Connection timeout occurred: {err}{reset_color}")
    except requests.exceptions.Timeout as err:
        print(f"{red}Request timed out: {err}{reset_color}")
    except requests.exceptions.RequestException as e:
        print(f"{red}Request error: {e}{reset_color}")

    
    
    
    