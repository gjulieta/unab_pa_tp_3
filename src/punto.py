#crear la clase punto#
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def eje_x(self):
        return self.x

    def eje_y(self):
        return self.y

    def impresion(self):
        return f"({self.x}, {self.y})"

    def opuesto(self):
        return Punto(-self.x, -self.y)    