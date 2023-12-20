# Visualization for Oceanos NTUA 

This is a repository used to visualize several parameters of Oceanos NTUA Boat, 
such as Motor Temperature, Rounds per Minute of the Motor, that are required in
the MEBC 2024.

To run the visualization follow the steps below:

1. Git clone the repo 
2. Make a virtual environment as specified here [venv](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)
3. Install dependencies (requirements.txt) as specified in the link above
4. Run in a terminal the command `ngrok start oceanos` (after you follow the instructions for ngrok)
5. Run in a terminal the `dummy_server.py` python file for the ngrok server
6. Run `App.py` for the visualization 

(If you only want to see the simulation modes, you can omit steps 4,5)


This repository uses HTML, CSS , JavaScript and a JS library called roundSlider,
which is explained further below.

[Telemetry visualization](https://github.com/ntua-el20069/oceanos-visualization-2024/blob/main/templates/telemetry.html)

# roundSlider - A free jQuery plugin

Link: https://github.com/soundar24/roundSlider.git

You can run the demo for roundSlider: templates/demo.html
[Demo](https://github.com/ntua-el20069/oceanos-visualization-2024/blob/main/templates/demo.html)
