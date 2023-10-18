import math

class ShapeMeta(type):
    def __instancecheck__(self, instance):
        return self.__subclasscheck__(type(instance))

    def __subclasscheck__(self, subclass):
        return (hasattr(subclass, 'area') and callable(subclass.area))

class ShapeInterface(metaclass=ShapeMeta):
    pass

class Rectangle(ShapeInterface):
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def get_width(self):
        return self._width

    def set_width(self, width):
        self._width = width

    def get_height(self):
        return self._height

    def set_height(self, height):
        self._height = height

    def area(self):
        return self.get_width() * self.get_height()

class Circle(ShapeInterface):
    def __init__(self, radius):
        self._radius = radius

    def get_radius(self):
        return self._radius

    def set_radius(self, radius):
        self._radius = radius
    
    def area(self):
        return self.get_radius()*self.get_radius()*math.pi

class Rombo(ShapeInterface):
    def __init__(self,diagonalMayor,diagonalMenor):
        self._diagonalMayor=diagonalMayor
        self._diagonalMenor=diagonalMenor
    def get_diagonalMayor(self):
        return self._diagonalMayor
    def set_diagonalMayor(self,diagonalMayor):
        self._diagonalMayor=diagonalMayor
    def get_diagonalMenor(self):
        return self._diagonalMenor
    def set_diagonalMenor(self,diagonalMenor):
        self._diagonalMenor=diagonalMenor

class Triangulo(ShapeInterface):
    def __init__(self, base, altura):
        self._base = base
        self._altura= altura

    def get_base(self):
        return self._base

    def set_base(self, base):
        self._base = base

    def get_altura(self):
        return self._altura

    def set_altura(self, altura):
        self._altura = altura


    def area(self):
        return (self.get_base() * self.get_altura())/2

class Cuadrado(ShapeInterface):
    def __init__(self, lados):
        self._lados = lados

    def get_lados(self):
        return self._lados

    def set_lados(self, lados):
        self._lados = lados

    def area(self):
        return self.get_lados() * self.get_lados()


class Board():
    def __init__(self,shapes):
        self._shapes=shapes

    def calculateArea(self):
        area=0
        for shape in self._shapes:
            area+=shape.area()
        return area

if __name__=="__main__":
    
    alto=int(input("Ingrese la altura del rectángulo: "))
    ancho=int(input("Ingrese el ancho del rectángulo: "))
    rectangulo=Rectangle(alto,ancho)
    tablero=Board(rectangulo)
    print("El área del rectángulo es: ", rectangulo.area())
    radio=int(input("Ingrese el radio del círculo: "))
    circulo=Circle(radio)
    figura=[circulo,rectangulo]
    tablero=Board(figura)
    print("Área total: ", tablero.calculateArea())
    
    