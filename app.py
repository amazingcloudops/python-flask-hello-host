from flask import Flask, render_template
import socket

app = Flask(__name__)

@app.route('/')
def home():
    host = socket.gethostname()
    return render_template('index.html', host=host)

if __name__ == '__main__':
    app.run()