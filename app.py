from flask import Flask, render_template, json, redirect, url_for
from flask_socketio import SocketIO, emit

import serial
import serial.tools.list_ports

from display import Display
from canvas import Canvas

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Hemmelignoegle'
socketio = SocketIO(app)

arduino_ports = [p.device for p in serial.tools.list_ports.comports()]

display = Display(5, 5, arduino_ports[0], 9600);

canvas = Canvas(display)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reset')
def reset():
    canvas.reset()
    return redirect(url_for('index'))

def emitPixel(x, y, color):
    color = 'rgb({}, {}, {})'.format(color[0], color[1], color[2])
    data = json.dumps({"x": x, "y": y, "color": color})
    emit('setDisplay', data)

@socketio.on('user')
def user_connected(data):
    [[emitPixel(x, y, canvas.getPixel(x, y)) for x in range(9)] for y in range(9)]

@socketio.on('drawPixel')
def setPixel(data):
    emit('setPixel', data, broadcast=True)
    pixel = str(data).replace('\'', '"')
    pixel = json.loads(pixel)
    color = tuple([int(x) for x in pixel['color'][4:-1].split(', ')])
    canvas.setPixel(pixel['x'], pixel['y'], color)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=80)