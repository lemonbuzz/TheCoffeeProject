from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import RPi.GPIO as IO

IO.setmode(IO.BOARD)
IO.setup(40, IO.OUT)

power = False
IO.output(40, power)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

def togglePower():
    global power
    power = not power
    IO.output(40, power)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('togglePower')
def test_message(message):
    togglePower()
    emit('statusUpdate', power)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=80)
