
class QuadrilateroMeta(type):
    def __instancecheck__(self,instance):
        return self.__subclasscheck__(type(instance))

    def __subclasscheck__(self, subclass):
        return (hasattr(subclass,'area')and callable(subclass.area)) \
            and (hasattr(subclass,'get_height') and callable(subclass.get_height)) \
            and (hasattr(subclass,'get_width') and callable(subclass.get_width)) \
        

class Quadrilateralinterface(metaclass=QuadrilateroMeta):
    pass

class Rectangulo(Quadrilateralinterface):

    def __init__(self, ancho, altura):
        self._ancho = ancho
        self._altura = altura

    def get_ancho(self):
        return self._ancho

    def set_ancho(self, ancho):
        self._ancho = ancho

    def get_altura(self):
        return self._altura

    def set_altura(self, altura):
        self._altura = altura

    def area(self):
        return self.get_ancho() * self.get_altura()

class Cuadrado(Quadrilateralinterface):
    def __init__(self, ancho):
        self._ancho = ancho
        self._altura = ancho

    def get_ancho(self):
        return self._ancho

    def set_ancho(self, ancho):
        self._ancho = ancho
        self._altura = ancho

    def get_altura(self):
        return self._altura

    def set_altura(self, altura):
        self._altura = altura
        self._ancho = altura
    
    def area(self):
        return self.get_ancho() * self.get_altura()
        
if __name__ == '__main__':

    print("Para el rectángulo.")
    numRectangulos = int(input("Número de rectangulos: "))

    while (numRectangulos < 0):
        print("Error")
        numRectangulos = int(input("Rectángulos: "))

    sumaR = 0
    for longi in range (numRectangulos):

        ancho=float(input("Ingresar el lado del cuadrado: "))

        figuraR=Cuadrado(ancho)
        print("El área del Rectangulo [",(longi+1),"] es: ", figuraR.area())
        
        sumaR += figuraR.area()
    print("La suma de las áreas de los rectángulos es: ",sumaR)