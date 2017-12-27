class Canvas:
    """Matrice med farvevaerdier for pixels"""
    def __init__(self, display):
        self.display = display
        self.pixels = [[(255, 255, 255) for x in range(9)] for y in range(9)]
        [[self.display.xyPixel(x, y, (255, 255, 255)) for x in range(9)] for y in range(9)]

    def reset(self):
        self.pixels = [[(255, 255, 255) for x in range(9)] for y in range(9)]
        [[self.display.xyPixel(x, y, (255, 255, 255)) for x in range(9)] for y in range(9)]

    def getPixel(self, x, y):
        return self.pixels[x][y]

    def setPixel(self, x, y, color):
        self.pixels[x][y] = color
        self.display.xyPixel(x, y, color)