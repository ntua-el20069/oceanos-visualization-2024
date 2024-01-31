# Visualization for Oceanos NTUA 

This is a repository used to visualize several parameters of Oceanos NTUA Boat, 
such as Motor Temperature, Rounds per Minute of the Motor, that are required in
the MEBC 2024. It is hosted on web, to visit follow the link below:
[Oceanos Visualization Website](http://oceanosntua.pythonanywhere.com/)

## Quick Changes in the Code 

1. `useful.py`: Ctrl + F: `CHANGE` : to see how to change csv that is read, reading of last line of the csv `REAL_TIME` to have real time data (True) or not (False - simulate for development purposes), change significant paths. 
In addition, modify variables so as to select if you want to send to web-host (pythonanywhere) or client (e.g. your computer running client python code) or both. (If you do not send to client, you do not need to run ngrok and client code !). 
2. `App.py`: Ctrl + F : `CHANGE` : set `mode` to the value 'local' for Rasberry or your computer testing, 'client' for the PC running client code
3. [Add CSV in this Folder](https://github.com/ntua-el20069/oceanos-visualization-2024/tree/reverse-server/static/csv)   
4. [Javascript Files](https://github.com/ntua-el20069/oceanos-visualization-2024/tree/reverse-server/static/functions): <br>
        - Here you can change the visualization RELOAD PERIOD: `setInterval` (2nd argument is time in ms) in `events.js`. <br>
        - You can add a new data visualization (or change sequence) by adding a data in list `allData` in `data.js` (check the class definition of `Data`). <br>
        - You can change the display of the roundSliders in `display.js` after you check [roundSlider attributes](https://github.com/ntua-el20069/oceanos-visualization-2024/blob/reverse-server/static/dist/roundslider.js) <br>
5. [Styles](https://github.com/ntua-el20069/oceanos-visualization-2024/blob/reverse-server/static/styles/styles.css) <br>
        - Here you can change the text (font) size for visualization by changing the variable `--textSize`.

## Local visualization test
To run the visualization follow the steps below:

1. Git clone the repo 
2. Make a virtual environment as specified here [venv](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)
3. Install dependencies (`requirements.txt`) as specified in the link above (if anything throws error try removing it from `requirements.txt` - some dependencies are unnecessary)
4. Run in a terminal the command `ngrok start oceanos` (after you follow the instructions for ngrok)
5. Run in a terminal the `server.py` python file for the ngrok server (it is actually the code that will run in raspberry and send messages to client)
6. Run `App.py` for the visualization 
7. Run `client.py` to receive data as client PC
8. (Oprtional) If you want to run the program as a startup application (exactly after boot) you should copy the `.desktop` files which are in the `desktop` folder and paste them inside directory `~/.config/autostart` (in most Unix based systems) (and check that these files have execution permission)

(The visualization `App.py` can work without running ngrok and server)

## Raspberry Pi visualization test
1. Git clone the repo (if not cloned yet)
2. Try running `App.py` and `send_messages.py` (to see import errors) 
3. pip install all reported dependencies (continue until you do not have import errors)
4. In Raspberry, run in a terminal the command `ngrok start oceanos` (after you follow the instructions for ngrok)
5. In Raspberry Pi, run `App.py` for the visualization and `server.py` to send the data to client PC
6. In another computer, run in a terminal the `client.py` python file to receive data as a client
7. (Oprtional) If you want to run the program as a startup application (exactly after boot) you should copy the files: `virtualization.desktop` and `firefox.desktop` and `send.desktop` and `ngrok.desktop` which are in the `desktop` folder and paste them inside directory `~/.config/autostart` (in Raspberry Pi) (and check that these files have execution permission). <strong>Important!</strong> change the comments to use the correct `Exec` configuration in `.desktop` files.

```bash
git clone https://github.com/ntua-el20069/oceanos-visualization-2024.git
cd oceanos-visualization-2024/
```
Possible alternative for step 3:
```bash
pip install flask pandas requests
```

## ToDos for Correct Visualization Check (ensure continuous visualization)

1. Use `restart` files in the `Exec` configuration of the `.desktop` files (`ngrok.desktop` and `firefox.desktop`)
2. Repeat the steps for the Raspberry Pi that will run in MEBC (`xterm` may not be installed there)
3. Change code in `useful.py` (make `REAL_TIME = True`) so as to get real time data - read the last line of the CSV in which `gps_with_temp.py` writes.

## Deploy code in Web Host

1. In pythonanywhere account, delete the folder `/home/oceanosntua/oceanos-visualization-2024`
2. Write in bash console in Python `cd /home/oceanosntua/`
3. Git clone the repo: `git clone https://github.com/ntua-el20069/oceanos-visualization-2024.git`
4. Enter the repo directory: `cd oceanos-visualization-2024/`
5. In pythonanywhere file `/home/oceanosntua/oceanos-visualization-2024/App.py`: set `mode` to the value 'web' instead of 'local'
6. Reload the website from pythonanywhere reload button.
7. Run the <strong>local</strong> `server.py`.
8. Refresh the web page and you will see that data change in the Normal mode visualization!
9. (Optional) Before each of seatrials / MEBC race, download `/home/oceanosntua/hostdata.csv` in order to save it locally (and rename it!) and remove it from host folder because we want the next hostdata to refer to another race.

Bash commands for 1-5 in pythonanywhere bash console.
```bash
rm -r /home/oceanosntua/oceanos-visualization-2024
```
```bash
cd /home/oceanosntua/
git clone https://github.com/ntua-el20069/oceanos-visualization-2024.git
cd oceanos-visualization-2024/
vim App.py
```

## Basic Understanding of the data transmission to Web Host and client PC

- `server.py`:  code (that will run in raspberry) that sends messages to HOST or/and client (PC that runs client code)
- `helpers`: in this folder `sendWEB.py` is used to send the current json data to the HOST (web site) by HTTP POST request at endpoint `/send-data`  (This is probably similar to the way that we will send data to MEBC API). Host receives the request json data and writes them as the last line of a CSV file `hostdata.csv`.
- `client.py` : code (that we will run in our client PC) to receive data as client PC.

## Basic Understanding of the visualization

- `App.py` : builds a flask application that runs the backend code and sends response on requests to each specified route
- `templates/telemetry.html` : the basic HTML template of the visualization
- `static/functions` : includes JavaScript files that are executing to build the basic body of the visualization and execute reload functions to reload shown data. 
- `static/styles` : includes CSS files that define the style of the visualization
- `static/dist` : includes [roundSlider](https://github.com/soundar24/roundSlider.git), a free jQuery plugin
