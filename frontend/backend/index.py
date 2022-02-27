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
    f = open("output.txt", "w")
    subprocess.call(['docker-compose', 'run', 'python_service', 'python3', file_name], stdout=f)
    f = open("output.txt", "r")
    return f.read()

from pprint import pprint

@socket_.on("file_uploaded")
def handleFile(msg):
    print("Test file recieved",msg)
    with open("test.py", "w") as f:
        f.write(msg)
    res = execute_docker("test.py")
    emit("processing_done",res)
    return None


if __name__ == '__main__':
    socket_.run(app, debug=True, host='0.0.0.0', port=5001)
