# P2P Compute: Peer Application

React, Electron, Chakra Frontend with a Flask Backend

## Installation

```sh
python3 -m venv venv
pip3 install -r requirements.txt

npm install
```

## Run

### Backend

```
. venv/bin/activate
cd backend 
python index.py
```

### Frontend

```
. venv/bin/activate
npm start
```

## Resources
* [Socket.IO](https://socket.io/)
* Socket.IO v4: [Rooms](https://socket.io/docs/v4/rooms/), [Server API](https://socket.io/docs/v4/server-api/), [Client API](https://socket.io/docs/v4/client-api/)
* Flask-SocketIO: [Documentation](https://flask-socketio.readthedocs.io/en/latest/index.html), [GitHub](https://github.com/miguelgrinberg/Flask-SocketIO), [v4.3.1](https://github.com/miguelgrinberg/Flask-SocketIO/releases/tag/v4.3.1). We use v4.3.1 as the latest versions of Flask-SocketIO, Python SocketIO and Python EngineIO were not compatible with each other. [Suggested StackOverflow answer](https://stackoverflow.com/a/66497059/2806163).
* [Flask Session](https://flask-session.readthedocs.io/en/latest/)
* [Implement a WebSocket using Flask and Socket-IO](https://medium.com/swlh/implement-a-websocket-using-flask-and-socket-io-python-76afa5bbeae1)
* [Socket.IO P2P](https://socket.io/blog/socket-io-p2p/)
* [python-socketio](https://python-socketio.readthedocs.io/en/latest/client.html)
