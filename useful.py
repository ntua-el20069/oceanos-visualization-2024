fieldnames =["current_time", "latitude", "longitude", "speed", "miles", "miles_lap", "rtc", "millis", "rpm", "input_voltage", "motor_watt", "motor_tempMosfet", "motor_tempMotor", "motor_current", "battery_current","motor_dutyCycle", "motor_error", "rasp_temp", "battery_ampere", "battery_voltage", "charge", "battery_temperature", "autonomy"]

MEBC_fieldnames = ["temp1","temp2","temp3","voltage","current","lat","lon","team"]

IP = '127.0.0.1' # CHANGE ! IP is the IP of the MEBC_API server
PORT = '5000'   # CHANGE ! PORT is the PORT of the MEBC_API server
MEBC_API_url = f"http://{IP}:{PORT}/monitoringdata"
team_token = '# Here we will place the token of our team'  # CHANGE ! team_token is the token of our team in MEBC_API

#csv_url = 'static/csv/serverdata_2023-12-17_16-11-34.csv'  ### CHANGE with the path of the CSV you want to visualize Live (Normal Mode) (as Raspberry)
csv_url = 'static/csv/merged_file.csv'  

client_read_csv_path = 'clientdata.csv'                     ### CHANGE with the path of the CSV you want to visualize Live (Normal Mode) (as a client PC)

host_read_csv_path = f'/home/oceanosntua/hostdata.csv'

data_response_delimiter = '### Web Host says ###'

red = "\033[31m"
blue = "\033[34m"
yellow = "\033[33m"
magenta = "\033[35m"
reset_color = "\033[0m"

send_to_MEBC_API = True  # CHANGE ! MEBC_API is the server of the MEBC 
send_to_client = True  # CHANGE ! client is the computer in which we run client python code (receive messages via TCP)
send_to_host = True   # CHANGE ! host is the website (pythonanywhere) in which data are sent with HTTP POST request

delay = 0.5     # this is the MIN delay of sending data to client or/and host (MAX depends on HTTP request response time - set timeout there in helpers/sendWEB.py )  
                # consider that HTTP request takes approximately 0.4 sec to complete
                # (For reload time check JS files) 
                # I think it is not that important to CHANGE this (delay of taking data from CSV) 
                # 8ewroume mia ka8ysterhsh, an den mas aresei thn allazoyme

mode = 'local' # CHANGE ! mode is 'local' or 'web' depending on if we want to run the script in our local computer or in host (pythonanywhere)
                            # 'client' if you run it in client (one of our PC that runs client code)

pre_path = '/home/oceanosntua/oceanos-visualization-2024/' if mode == 'web' else ''  # CHANGE !  Set the path of the project in the host (pythonanywhere) 

REAL_TIME = False        #   CHANGE !   Set to True if you want to take Real Time Data (last line of CSV) , when False it just simulates the csv ...