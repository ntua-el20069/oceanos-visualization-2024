import requests
import time

green = "\033[32m"
red = "\033[31m"
# Reset ANSI escape code for default text color
reset_color = "\033[0m"

def send_website(data_now: dict):
    start = time.time()
    try: 
        response = requests.post(
            'http://oceanosntua.pythonanywhere.com/send-data',
            json=data_now,
            timeout=1
        )
        response.raise_for_status() 
        end = time.time()

        response_text = response.content.decode('utf-8')
        
        out = f'{green} HTTP POST {reset_color} Request Response: (Time consumed: {green} {(end-start):.3f} seconds {reset_color})\t Response: '
        color = green if 'OK' in response_text else red
        out += f"{color}{response_text}{reset_color}"
    
    except requests.exceptions.ConnectTimeout as err:
        out = f"Response: {red}Connection timeout occurred: {err}{reset_color}\n"
    except requests.exceptions.Timeout as err:
        out = f"Response: {red}Request timed out: {err}{reset_color}\n"
    except requests.exceptions.RequestException as e:
        out = f"Response: {red}Request error: {e}{reset_color}\n"
    return out

    
    
    
    