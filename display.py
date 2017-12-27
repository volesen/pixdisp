import serial
import serial.tools.list_ports

class Display:
    def __init__(self, width, height, port, baud):
        self.width = width
        self.height = height
        self.arduino = serial.Serial(port, baud)
    
    def xyToId(self, x, y):
        if y%2 == 0:
            id = x + y * self.width
        else:
            id = (self.width - x) + (y * self.width) - 1
        return id
    
    def write(self = 0, cmd = 0, id = 0, r = 0, g = 0, b = 0):
        self.arduino.write(b'%d,%d,%d,%d,%d\n' % (cmd, id, r, g, b))
        
    def update(self):
        self.write(3)
    
    def clear(self):
        self.arduino.write(b'%d,%d,%d,%d,%d\n' % (2, 0, 0, 0, 0))
    
    def setPixel(self, id, r, g, b):
        """ Sets a pixel in buffer, but does not display. Faster that updatePixel """
        self.write(0, id, r, g ,b)
    
    def updatePixel(self, id, r, g, b):
        """ Sets and shows pixel. """
        self.write(1, id, r, g ,b)
    
    def xyPixel(self, x, y, color):
        id = self.xyToId(x, y)
        self.updatePixel(id, color[0], color[1], color[2])
    
    def close(self):
        self.arduino.close()