
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Oceanos NTUA!'

app.route('/demo')
def telemetry_demo():
    render_template('')

if __name__ == '__main__':
    app.run(debug=True)

         
