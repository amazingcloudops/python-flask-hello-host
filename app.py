from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    host = request.headers.get('Host').split(':')[0]
    return render_template('index.html', host=host)

if __name__ == '__main__':
    app.run()