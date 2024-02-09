fieldnames =["current_time", "latitude", "longitude", "speed", "miles", "miles_lap", "rtc", "millis", "rpm", "input_voltage", "motor_watt", "motor_tempMosfet", "motor_tempMotor", "motor_current", "battery_current","motor_dutyCycle", "motor_error", "rasp_temp", "battery_ampere", "battery_voltage", "charge", "battery_temperature", "autonomy"]

MEBC_fieldnames = []
IP = ''
PORT = ''
MEBC_API_url = f"http://{IP}:{PORT}/monitoringdata/"

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

send_to_MEBC_API = False  # CHANGE ! MEBC_API is the server of the MEBC 
send_to_client = True  # CHANGE ! client is the computer in which we run client python code (receive messages via TCP)
send_to_host = True   # CHANGE ! host is the website (pythonanywhere) in which data are sent with HTTP POST request

delay = 0.5     # this is the MIN delay of sending data to client or/and host (MAX depends on HTTP request response time - set timeout there in helpers/sendWEB.py )  
                # consider that HTTP request takes approximately 0.4 sec to complete
                # (For reload time check JS files) 
                # I think it is not that important to CHANGE this (delay of taking data from CSV) 
                # 8ewroume mia ka8ysterhsh, an den mas aresei thn allazoyme

REAL_TIME = False        #   CHANGE !   Set to True if you want to take Real Time Data (last line of CSV) , when False it just simulates the csv ...