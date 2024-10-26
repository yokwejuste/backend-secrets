from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on('message')
def handle_message(msg):
    print(f"Received message: {msg}")

if __name__ == '__main__':
    socketio.run(app)
