# Visualization for Oceanos NTUA 

This is a repository used to visualize several parameters of Oceanos NTUA Boat, 
such as Motor Temperature, Rounds per Minute of the Motor, that are required in
the MEBC 2024.

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

# Rasberry Pi visualization test
1. Git clone the repo (if not cloned yet)
2. Try running `App.py` for the visualization (to see import errors) 
3. pip install all reported dependencies (continue until you do not have import errors)
4. In another computer, run in a terminal the command `ngrok start oceanos` (after you follow the instructions for ngrok)
5. In another computer (in which you run ngrok), run in a terminal the `dummy_server.py` python file for the ngrok server
6. In Rasberry Pi, run `App.py` for the visualization 
7. (Oprtional) If you want to run the program as a startup application (exactly after boot) you should copy the files: `virtualization.desktop` and `firefox.desktop` which are in the `desktop` folder and paste them inside directory `~/.config/autostart` (in Rasberry Pi) (and check that these files have execution permission). Important: change the comments to use the correct `Exec` configuration in `.desktop` files.

# ToDos for Correct Visualization Check (ensure continuous visualization)

1. Use the `restart` files in the `Exec` configuration of the `.desktop` files (`virtualization.desktop` and `firefox.desktop`)
2. Repeat the steps for the Rasberry Pi that will run in MEBC (`xterm` may not be installed there)
3. Change code in `App.py` and `dummy_server.py` (or use `Final_server.py`) so as to read the last line of the CSV in which `gps_with_temp.py` writes.

# Quick Changes in the Code 

1. `App.py`: Ctrl + F : `CHANGE` to see how to change csv that is read, reading of last line of the csv, change the period in which csv lines are read and sent to the server.
2. [Add CSV in this Folder](https://github.com/ntua-el20069/oceanos-visualization-2024/tree/main/static/csv)   
3. [Javascript Files](https://github.com/ntua-el20069/oceanos-visualization-2024/tree/main/static/functions): 
        - Here you can change the visualization RELOAD PERIOD: `setInterval` (2nd argument is time in ms) in `events.js`. 
        - You can add a new data visualization by adding a data in lists `datalist` or `numericData` in `data.js` (check the class definition of `Data`). 
        - You can change the display of the roundSliders in `display.js` after you check [roundSlider attributes](https://github.com/ntua-el20069/oceanos-visualization-2024/blob/main/static/dist/roundslider.js)

This repository uses HTML, CSS , JavaScript and a JS library called roundSlider,
which is explained further below.

[Quick telemetry visualization demo simulation only](https://oceanos-visualization-demo.netlify.app/)

[Telemetry visualization code](https://github.com/ntua-el20069/oceanos-visualization-2024/blob/main/templates/telemetry.html)

# roundSlider - A free jQuery plugin

Link: https://github.com/soundar24/roundSlider.git

You can run the demo for roundSlider: templates/demo.html
[Demo code](https://github.com/ntua-el20069/oceanos-visualization-2024/blob/main/templates/demo.html)
