from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit, disconnect, send
import subprocess
from pprint import pprint

async_mode = None
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socket_ = SocketIO(app, cors_allowed_origins="*")
app.debug = True
app.host = 'localhost'
clients = []

@app.route('/')
def index():
    return render_template('index.html', async_mode=socket_.async_mode)

def execute_docker(file_name):
    subprocess.call(['docker-compose', 'build'])
    f = open("output.txt", "w")
    subprocess.call(['docker-compose', 'run', 'python_service', 'python3', file_name], stdout=f)
    f = open("output.txt", "r")
    return f.read()

@socket_.on('connected')
def connected():
    print(f"{request.sid} connected")
    print("[before append] clients:",clients)
    clients.append(request.sid)
    print("[after append] clients:",clients)

# does this ever get triggerred???
@socket_.on('disconnect')
def disconnect():
    print(f"{request.sid} disconnected")
    print("[before remove] clients:",clients)
    if request.sid in clients:
        clients.remove(request.sid)
    print("[after remove] clients:",clients)

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
