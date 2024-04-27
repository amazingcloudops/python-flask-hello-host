from flask import Flask, render_template
import socket, os

app = Flask(__name__)

@app.route('/')
def home():
    hostname = socket.gethostname()
    custom_header = os.environ.get('CUSTOM_HEADER')
    return render_template('index.html', hostname=hostname, custom_header=custom_header)

if __name__ == '__main__':
    app.run()