
from flask import Flask, render_template, redirect, url_for, jsonify, request
from helpers.readCSV import readCSV
from useful import *

mode = 'local' # CHANGE ! mode is 'local' or 'web' depending on if we want to run the script in our local computer or in host (pythonanywhere)
                            # 'client' if you run it in client (one of our PC that runs client code)

app = Flask(__name__)
    
@app.route('/')  # basic web route
def home():
    return render_template('telemetry.html') 

@app.route('/reload') # reload data, update visualization (a JavaScript function fetches this JSON data every 1 sec)
def reload():  
    print(f"{yellow}Javascript Reload{reset_color}")
    if mode == 'local':
        return jsonify(readCSV(csv_url, fieldnames, realTime = REAL_TIME, delay = delay))
    elif mode == 'client':
        return jsonify(readCSV(client_read_csv_path, fieldnames, realTime = True))
    else: # 'web' mode
        return jsonify(readCSV(host_read_csv_path, fieldnames, realTime = True))  

@app.route('/send-data', methods = ['POST'])
def send_data():
    try:
        request_data = request.get_json()
        separator = ','
        csv_line = separator.join(list(request_data.values())).replace('nan','')
        with open(host_read_csv_path,'a',encoding='utf-8') as csvFile:
            print(f"{csv_line}", file=csvFile)     
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

@app.route('/make-diagram', methods = ['POST']) # make diagram route
def make_diagram():
    # TODO: this route should make the demanded diagram by the form and redirect to it
    pass

@app.route('/diagram-test') # test route
def diagramTest():
    return render_template('diagrams/current_with_temp/motor_current_with_motor_tempMosfet.html')

if __name__ == '__main__':
    # Start separate thread for visualization
    #web_thread = Thread(target=visualization, args=())
    #web_thread.start()
    

    
    # Local host (our computer) visualization - not network accessible
    # If we run this in our local computer, we can access the site via http://localhost:5000/ 
    # app.run(debug=True)



    # if we run this below, all devices in the same network (connected to the same router) 
    # can access the site via http://{local-network-IP}:5000/       
    # most times it is http://192.168.1.11:5000/
    # you can find your local network IP by typing ipconfig in cmd (windows) or ifconfig in terminal (linux)
    # or hostname -I in terminal (linux)
    # or in windows go to network settings and find your IP
    app.run(host='0.0.0.0', use_reloader=False, debug=True)
    
    

