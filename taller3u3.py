import math
class ShapeMeta(type):

    def __instancecheck__(self, instance):
        return self.__subclasscheck__(type(instance))

    def __subclasscheck__(self, subclass):
        return (hasattr(subclass, 'area') and
        callable(subclass.area))

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
        return self.get_radius() * self.get_radius() * math.pi




class Rombo(ShapeInterface):
    def __init__(self, diagonalMenor, diagonalMayor):
        self._diagonalMenor = diagonalMenor
        self._diagonalMayor = diagonalMayor

    def get_diagonalMenor(self):
        return self._diagonalMenor

    def set_diagonalMenor(self, diagonalMenor):
        self._diagonalMenor = diagonalMenor

    def get_diagonalMayor(self):
        return self._diagonalMayor

    def set_diagonalMayor(self, diagonalMayor):
        self._diagonalMayor = diagonalMayor


    def area(self):
        return (self.get_diagonalMenor() * self.get_diagonalMayor())/2


class Cuadrado(ShapeInterface):
    def __init__(self, lados):
        self._lados = lados

    def get_lados(self):
        return self._lados

    def set_lados(self, lados):
        self._lados = lados

    def area(self):
        return self.get_lados() * self.get_lados()


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




class Board():
    def __init__(self,shapes):
        self._shapes=shapes

    def calculateArea(self):
        area=0

        for shape in self._shapes:
            area+=shape.area()
        return area


'''Creamos el if main'''
if __name__=="__main__":

    print("========================== \n Menu Principal: \n==========================  \n 1- Rectangulo \n 2- Circulo \n 3- Rombo \n 4- Cuadrado \n 5- Triangulo \n ==========================  \n Opcion: ")

    numeroFiguras=int(input("Cuantas figuras desea utilizar: "))
    lista=[]
    numeros=True

    while numeros == True:

            for i in range(numeroFiguras):

            
                opcionesSeleccionadas=int(input("ingrese numeros a seleccionar: "))
                lista.append(opcionesSeleccionadas)

            numeros=False

    listaFiguras=[]
    print("\n")

    
    if 1 in lista:

        '''Ingresamos datos de altura, anchura y radio'''
        
        valorAltura=int(input("Ingresar la altura del rectangulo: "))
        valorAncho=int(input("Ingresar el ancho del rectangulo: "))

        '''Instanciamos figura 1 rectangulo'''
        figura1=Rectangle(valorAltura,valorAncho)

        print("Area total calculada rectangulo: ",figura1.area())

        listaFiguras.append(figura1)
        print("\n")

    if 2 in lista:

        
        valorRadio=float(input("Ingrese valor del radio: "))
        '''Instanciamos figura 2 circulo'''
        figura2=Circle(valorRadio)

        print("Radio del circulo total: ",figura2.area())

        listaFiguras.append(figura2)
        print("\n") 

    if 3 in lista:

        
        valorDiagonalMenor=float(input("Ingrese valor de daigonal menor del Rombo: "))
        valorDiagonalMayor=float(input("Ingrese valor de daigonal Mayor del Rombo: "))

        figura3=Rombo(valorDiagonalMenor,valorDiagonalMayor)

        print("Area total calculada del rombo: ",figura3.area())

        listaFiguras.append(figura3)
        print("\n")

    if 4 in lista:

        
        valorLados=int(input("Ingresar lados de un cuadrado: "))
        figura4=Cuadrado(valorLados)

        print("Area total calculada del cuadrado: ",figura4.area())

        listaFiguras.append(figura4)
        print("\n")

    if 5 in lista:

        
        valorBase=float(input("Ingrese valor base del Triangulo: "))
        valorAlturaTriangular=float(input("Ingrese valor altura del Triangulo: "))

        figura5=Triangulo(valorBase,valorAltura)
        print("Area total calculada del Triangulo: ",figura5.area())

        listaFiguras.append(figura5)
        print("\n")

    
    else:
        print("Usted no a sleccionado o sobrepaso los limites ninguna figura")



    '''Instanciamos Board con la lista de Figuras'''
    valorBoard=Board(listaFiguras)

    '''Imprimimos las sumas de las 2 areas'''
    print("shape calculado final total: ",valorBoard.calculateArea())

    
