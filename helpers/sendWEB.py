import requests
import time

green = "\033[32m"
magenta = "\033[35m"
red = "\033[31m"
# Reset ANSI escape code for default text color
reset_color = "\033[0m"
our_website = 'http://oceanosntua.pythonanywhere.com/send-data'

def send_website(data_now: dict, url = our_website):
    start = time.time()
    try: 
        response = requests.post(
            url,
            json=data_now,
            timeout=1
        )
        response.raise_for_status() 
        end = time.time()

        response_text = response.content.decode('utf-8')
        
        color = green if url == our_website else magenta
        out = f'{color} HTTP POST {reset_color} Request Response: (Time consumed: {color} {(end-start):.3f} seconds {reset_color})\t Response: '
        if 'error' in response_text:
            color = red
        out += f"{color}{response_text}{reset_color}"
    
    except requests.exceptions.ConnectTimeout as err:
        out = f"Response: {red}Connection timeout occurred: {err}{reset_color}\n"
    except requests.exceptions.Timeout as err:
        out = f"Response: {red}Request timed out: {err}{reset_color}\n"
    except requests.exceptions.RequestException as e:
        out = f"Response: {red}Request error: {e}{reset_color}\n"
    return out

    
    
    
    