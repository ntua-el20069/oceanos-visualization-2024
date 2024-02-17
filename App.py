
from flask import Flask, render_template, redirect, url_for, jsonify, request
from helpers.readCSV import readCSV
from useful import *
from Diagrams import statistics_plots, current_with_temp2
import pandas as pd
from datetime import datetime

app = Flask(__name__)
    
data_now = {}

@app.route('/')  # basic web route
def home():
    return render_template('telemetry.html') 

@app.route('/reload') # reload data, update visualization (a JavaScript function fetches this JSON data every 1 sec)
def reload():  
    global data_now
    print(f"{yellow}Javascript Reload{reset_color}")
    if mode == 'local':
        return jsonify(readCSV(csv_url, fieldnames, realTime = REAL_TIME, delay = delay))
    elif mode == 'client':
        return jsonify(readCSV(client_read_csv_path, fieldnames, realTime = True))
    else: # 'web' mode
        ## CAUTION: this global variable should be returned only if we deploy with only one worker
        return data_now
        #return jsonify(readCSV(host_read_csv_path, fieldnames, realTime = True))  

@app.route('/send-data', methods = ['POST'])
def send_data():
    global data_now
    try:
        request_data = request.get_json()
        separator = ','
        csv_line = separator.join(list(request_data.values())).replace('nan','')
        with open(host_read_csv_path,'a',encoding='utf-8') as csvFile:
            print(f"{csv_line}", file=csvFile)     
        data_now = request_data
    except Exception as e:
        return jsonify({"message" : f'Error: {e}'}), 400 
    return jsonify({"message" : 'OK'}), 200    


@app.route('/example') # example about how fetch & reload works
def example():
    return render_template('example.html')

@app.route('/roundSlider') # roundSlider demo for different types of circular inputs
def roundSlider():
    return render_template('demo.html')

# TODO : A .html page where we select (in an HTML form) the following:
#           1. the time period (start date time , end date time)
#           2. the type of plots we want to see (line, scatter, current_with_temp)
#           3. the data we want to see (motor_current, motor_temp, battery_current, battery_temp, battery_voltage, etc) from the fieldnames list
#       and will make a POST request to '/make-diagram'  

@app.route('/select-diagram') # select diagram route
def select_diagram():
    return render_template('diagram-select.html')

@app.route('/make-diagram', methods = ['POST']) # make diagram route
def make_diagram():
    # TODO: this route should make the demanded diagram by the form and redirect to it
    try:
        start_datetime = request.form['startDateTime']
        end_datetime = request.form['endDateTime']
        type = request.form['plotType']
        field = request.form['dataSelection']

        # change datetime format to match the one in the csv file
        datetime_format = "%Y-%m-%dT%H:%M"
        start_datetime = datetime.strptime(start_datetime, datetime_format)
        end_datetime = datetime.strptime(end_datetime, datetime_format)

        start_time = start_datetime.time()
        end_time = end_datetime.time()
        print(f"Start : {start_time},       End :  {end_time}")

        start_timedelta = pd.to_timedelta(str(start_time))
        end_timedelta = pd.to_timedelta(str(end_time))

        if type == 'line' or type == 'scatter':
            statistics_plots(start_timedelta , end_timedelta , field, type)
        elif type == 'current_with_temp':
            current_with_temp2(start_timedelta, end_timedelta)
        else:
            pass
        return redirect(f'/diagram/{type}/{field}')
        #return jsonify({"message" : f'OK', "start": f"{start_time}", 'end': f"{end_time}", 'type': f"{type}", 'field': f"{field}"}), 200
        
    except Exception as e:
        return jsonify({"message" : f'Error: {e}', 'possible-solution': 'Check that input and select names in the form are as specified in /make-diagram route'}), 400

@app.route('/diagram-test') # test route
def diagramTest():
    return render_template('diagrams/current_with_temp/motor_current_with_motor_tempMosfet.html')

@app.route('/diagram/<type>/<field>') # diagram route
def diagram(type, field):
    path = f'diagrams/{type}/motor_current_with_{field}.html' if type == 'current_with_temp' else f'diagrams/statics/{type}/{field}.html'
    with open(path, 'r') as file:
        diagram = file.read()
        return diagram

if __name__ == '__main__':
    # Start separate thread for visualization
    #web_thread = Thread(target=visualization, args=())
    #web_thread.start()
    

    
    # Local host (our computer) visualization - not network accessible
    # If we run this in our local computer, we can access the site via http://localhost:5000/ 
    # app.run(debug=True)



    # if we run this below, all devices in the same network (connected to the same router) 
    # can access the site via http://{local-network-IP}:5000/       
    # most times it is something like http://192.168.1.11:5000/
    # you can find your local network IP by typing ipconfig in cmd (windows) or ifconfig in terminal (linux)
    # or hostname -I in terminal (linux)
    # or in windows go to network settings and find your IP
    app.run(host='0.0.0.0', use_reloader=False, debug=True)
    
    

