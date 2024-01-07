from requestsAPI.account import account_info

fieldnames =["current_time", "latitude", "longitude", "speed", "miles", "miles_lap", "rtc", "millis", "rpm", "input_voltage", "motor_watt", "motor_tempMosfet", "motor_tempMotor", "motor_current", "battery_current","motor_dutyCycle", "motor_error", "rasp_temp", "battery_ampere", "battery_voltage", "charge", "battery_temperature", "autonomy"]

csv_url = 'static/csv/serverdata_2023-12-17_16-11-34.csv'  ### CHANGE with the path of the CSV you want to visualize Live (Normal Mode)

server_read_csv_path = 'serverdata.csv'                     ### CHANGE with the path of the CSV you want to visualize Live (Normal Mode) as a server PC

host_write_csv_path = 'hostdata.csv'
host_read_csv_path = f'/home/oceanosntua/oceanos-visualization-2024/static/csv/{host_write_csv_path}'

username, token, path = account_info()
console_id = 31700465 # CHANGE ! console_id  of  pythonanywhere (HOST)

red = "\033[31m"
blue = "\033[34m"
yellow = "\033[33m"
reset_color = "\033[0m"

send_to_server = True  # CHANGE ! server is the computer in which we run server python code (receive messages via TCP)
send_to_host = True   # CHANGE ! host is the website (pythonanywhere) in which data are sent with HTTP POST request

if send_to_host: delay = 1      # Changing this will not help, because HTTP request takes approximately 1 sec to complete
else : delay = 0.5              # (For reload time check JS files) I think it is not that important to CHANGE this (delay of taking data from CSV) (if we send the data ONLY to the server)

REAL_TIME = False        #   CHANGE !   Set to True if you want to take Real Time Data (last line of CSV) , when False it just simulates the csv ...