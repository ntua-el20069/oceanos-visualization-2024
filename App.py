
from flask import Flask, render_template, redirect, url_for, jsonify
from threading import Thread
from helpers.readCSV import readCSV
from useful import *

mode = 'local' # CHANGE ! mode is 'local' or 'web' depending on if we want to run the script in our local computer or in host (pythonanywhere)
                            # 'server' if you run it in server (one of our PC that runs server code)

app = Flask(__name__)
    
@app.route('/')  # basic web route
def home():
    return render_template('telemetry.html') 

@app.route('/reload') # reload data, update visualization (a JavaScript function fetches this JSON data every 1 sec)
def reload():  
    print(f"{yellow}Javascript Reload{reset_color}")
    if mode == 'local':
        return jsonify(readCSV(csv_url, fieldnames, realTime = REAL_TIME, delay = delay))
    elif mode == 'server':
        return jsonify(readCSV(server_read_csv_path, fieldnames, realTime = True))
    else: # 'web' mode
        return jsonify(readCSV(host_read_csv_path, fieldnames, realTime = True))  

@app.route('/example') # example about how fetch & reload works
def example():
    return render_template('example.html')

@app.route('/roundSlider') # roundSlider demo for different types of circular inputs
def roundSlider():
    return render_template('demo.html')

def visualization():
    app.run(host='0.0.0.0', use_reloader=False, debug=True)

if __name__ == '__main__':
    # Start separate thread for visualization
    #web_thread = Thread(target=visualization, args=())
    #web_thread.start()
    app.run(debug=True)

    
    

