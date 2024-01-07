# Visualization for Oceanos NTUA 

This is a repository used to visualize several parameters of Oceanos NTUA Boat, 
such as Motor Temperature, Rounds per Minute of the Motor, that are required in
the MEBC 2024. It is hosted on web, to visit follow the link below:
[Oceanos Visualization Website](http://oceanosntua.pythonanywhere.com/)

# Quick Changes in the Code 

1. `useful.py`: Ctrl + F: `CHANGE` : to see how to change csv that is read, reading of last line of the csv `REAL_TIME`, change significant paths. 
In addition, modify variables so as to select if you want to send to web-host (pythonanywhere) or server (e.g. your computer running server python code) or both. (If you do not send to server, you do not need to run ngrok and server code !). Finally you can change the `console_id` with the id of a pythonanywhere console that is open.
2. `App.py`: Ctrl + F : `CHANGE` : set `mode` to the value 'local' for Rasberry or your computer testing, 'server' for the PC running server code
3. [Add CSV in this Folder](https://github.com/ntua-el20069/oceanos-visualization-2024/tree/main/static/csv)   
4. [Javascript Files](https://github.com/ntua-el20069/oceanos-visualization-2024/tree/main/static/functions): <br>
        - Here you can change the visualization RELOAD PERIOD: `setInterval` (2nd argument is time in ms) in `events.js`. <br>
        - You can add a new data visualization (or change sequence) by adding a data in list `allData` in `data.js` (check the class definition of `Data`). <br>
        - You can change the display of the roundSliders in `display.js` after you check [roundSlider attributes](https://github.com/ntua-el20069/oceanos-visualization-2024/blob/main/static/dist/roundslider.js) <br>
5. [Styles](https://github.com/ntua-el20069/oceanos-visualization-2024/blob/main/static/styles/styles.css) <br>
        - Here you can change the text (font) size for visualization by changing the variable `--textSize`.

# Local visualization test
To run the visualization follow the steps below:

1. Git clone the repo 
2. Make a virtual environment as specified here [venv](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)
3. Install dependencies (`requirements.txt`) as specified in the link above (if anything throws error try removing it from `requirements.txt` - some dependencies are unnecessary)
4. Run in a terminal the command `ngrok start oceanos` (after you follow the instructions for ngrok)
5. Run in a terminal the `dummy_server.py` python file for the ngrok server
6. Run `App.py` for the visualization 
7. (Oprtional) If you want to run the program as a startup application (exactly after boot) you should copy the `.desktop` files which are in the `desktop` folder and paste them inside directory `~/.config/autostart` (in most Unix based systems) (and check that these files have execution permission)

(If you only want to see the simulation modes, you can omit steps 4,5)

# Raspberry Pi visualization test
1. Git clone the repo (if not cloned yet)
2. Try running `App.py` for the visualization (to see import errors) 
3. pip install all reported dependencies (continue until you do not have import errors)
4. In another computer, run in a terminal the command `ngrok start oceanos` (after you follow the instructions for ngrok)
5. In another computer (in which you run ngrok), run in a terminal the `dummy_server.py` python file for the ngrok server
6. In Raspberry Pi, run `App.py` for the visualization 
7. (Oprtional) If you want to run the program as a startup application (exactly after boot) you should copy the files: `virtualization.desktop` and `firefox.desktop` which are in the `desktop` folder and paste them inside directory `~/.config/autostart` (in Raspberry Pi) (and check that these files have execution permission). Important: change the comments to use the correct `Exec` configuration in `.desktop` files.

# ToDos for Correct Visualization Check (ensure continuous visualization)

1. Use the `restart` files in the `Exec` configuration of the `.desktop` files (`ngrok.desktop` and `firefox.desktop`)
2. Repeat the steps for the Raspberry Pi that will run in MEBC (`xterm` may not be installed there)
3. Change code in `App.py` and `dummy_server.py` (or use `Final_server.py`) so as to read the last line of the CSV in which `gps_with_temp.py` writes.

# Basic Understanding of Code for Web Host (Beta) 

1. `send_messages.py`: Local code that sends messages to HOST or/and Server 
2. `requestsAPI`: in this folder `send.py` is used to send the current data to the HOST by writing them as the last line of a CSV file in HOST (this is done by an HTTP request to the  API of pythonanywhere console to write a bash command).

# Deploy code in Web Host (Beta)

1. In pythonanywhere account, delete the folder `/home/oceanosntua/oceanos-visualization-2024`
2. Open a bash console in Python and type `cd /home/oceanosntua/`
3. Git clone the repo: `git clone https://github.com/ntua-el20069/oceanos-visualization-2024.git`
4. Enter the repo directory: `cd oceanos-visualization-2024/` and switch to branch web: `git checkout web`
5. In pythonanywhere file `/home/oceanosntua/oceanos-visualization-2024/App.py`: set `mode` to the value 'web' instead of 'local'
6. Start a bash console in pythonanywhere, and type `cd /home/oceanosntua/oceanos-visualization-2024/static/csv`
7. Take the id of that console (ensure that this console will not close)
8. In your <strong>local</strong> `App.py`, set `console_id` to the id of the console you opened above
9. Reload the website from pythonanywhere reload button, and it is ready.
10. Run the <strong>local</strong> `send_messages.py` to see changes in the Normal mode visualization (check `Basic Understanding of Code for Web Host`).
11. Refresh the web page



This repository uses HTML, CSS , JavaScript and a JS library called roundSlider,
which is explained further below.

[Quick telemetry visualization demo simulation only](https://oceanos-visualization-demo.netlify.app/)

[Telemetry visualization code](https://github.com/ntua-el20069/oceanos-visualization-2024/blob/main/templates/telemetry.html)

# roundSlider - A free jQuery plugin

Link: https://github.com/soundar24/roundSlider.git

You can run the demo for roundSlider: templates/demo.html
[Demo code](https://github.com/ntua-el20069/oceanos-visualization-2024/blob/main/templates/demo.html)
