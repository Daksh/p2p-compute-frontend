GLOBAL_PORT = '5252'
GLOBAL_IP = 'http://192.168.39.112'

from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit, disconnect, send
import subprocess, socketio

async_mode = None
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socket_ = SocketIO(app, cors_allowed_origins="*")
app.debug = True
app.host = 'localhost'
clients = []

# client to connect with the global/central server
sio = socketio.Client()

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

@socket_.on('disconnect')
def disconnect():
    print(f"{request.sid} disconnected")
    print("[before remove] clients:",clients)
    if request.sid in clients:
        clients.remove(request.sid)
    print("[after remove] clients:",clients)

@socket_.on("file_uploaded")
def handleFile(file):
    print("Test file recieved: ",file)
    sio.emit('send_file_to_global', file)

@socket_.on("register_this_machine")
def handleRegisterRequest():
    print("register_this_machine request received")
    sio.emit('register_compute')

@socket_.on("unregister_this_machine")
def handleUnregisterRequest():
    sio.emit('unregister_compute')

@sio.event
def connect():
    print("I'm connected!")

@sio.event
def connect_error(data):
    print("The connection failed!")

@sio.event
def disconnect():
    print("I'm disconnected!")

@sio.on('send_file_to_local')
def receive_file(file):
    print('I received a file!')
    with open("test.py", "w") as f:
        f.write(file)
    res = execute_docker("test.py")
    sio.emit('send_result_to_global', res)

@sio.on('send_result_to_local')
def receive_result(res):
    socket_.emit("processing_done", res, broadcast=True)

if __name__ == '__main__':
    sio.connect(GLOBAL_IP+':'+GLOBAL_PORT) # global host
    socket_.run(app, debug=True, host='0.0.0.0', port=5001)
