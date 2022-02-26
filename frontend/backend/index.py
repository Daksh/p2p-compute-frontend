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


@app.route('/docker_execution')
def index_execution():
    file_name = ""
    subprocess.Popen(['docker-compose', 'build', '.'])
    subprocess.Popen(['docker-compose', 'run', 'python_service', 'python3', file_name])

    return ""



@socket_.on("message")
def handleMessage(msg):
    print(msg)
    send(msg, broadcast=True)
    return None



if __name__ == '__main__':
    socket_.run(app, debug=True, host='0.0.0.0')
