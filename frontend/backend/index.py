from flask import Flask, render_template, session, copy_current_request_context
from flask_socketio import SocketIO, emit, disconnect, send
import subprocess

async_mode = None
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socket_ = SocketIO(app, cors_allowed_origins="*")
app.debug = True
app.host = 'localhost'

@app.route('/')
def index():
    return render_template('index.html', async_mode=socket_.async_mode)


def execute_docker(file_name):
    subprocess.call(['docker-compose', 'build'])
    p2 = subprocess.call(['docker-compose', 'run', 'python_service', 'python3', file_name])
    print(p2)

    return ""

from pprint import pprint

@socket_.on("file_recieve")
def handleFile(msg):
    print("Test file recieved",msg)
    with open("test.py", "w") as f:
        f.write(msg)
    execute_docker("test.py")
    return None

@socket_.on("message")
def handleMessage(msg):
    pprint(msg)
    send(msg, broadcast=True)
    return None



if __name__ == '__main__':
    socket_.run(app, debug=True, host='0.0.0.0')
