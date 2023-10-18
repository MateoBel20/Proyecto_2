'''
Se importa la clase abstracta ABC, la cual obliga 
a las subclases a implementar todos los métodos 
abstractos que se necesiten.
'''
from abc import ABC, abstractmethod

class Figura (ABC):
    '''
    Se crea una clase abstracta denominada "Figura", la cual se encargará
    de contener los atributos de nuestra figura a construir.

    -----------------
    Métodos:
    -----------------
        __init__(self, ancho, alto): Construye los atributos de la clase 
                                    abstracta, tiene el decorador "@abstractmethod"
                                    el cual hace que nuestro método sea abstracto.
        area(self): Método vacío, que tiene el decorador "@abstractmethod", el cual 
                    lo hace un método abstracto. Servirá más adelante para poder calcular el 
                    área de los rectángulos que querramos.

    ----------
    Atributos:
    ----------
        ancho=int-> Variable que va almacenar el ancho de nuestra figura.

        alto=int-> Variable que va almacenar el alto de nuestra figura.
    '''
    @abstractmethod
    def __init__(self, ancho, alto):
        '''
        Construye los atributos de la clase 
        abstracta, tiene el decorador "@abstractmethod"
        el cual hace que nuestro método sea abstracto.

        -----------
        Parámetros:
        -----------
        ancho=int-> Variable que va almacenar el ancho de nuestra figura.

        alto=int-> Variable que va almacenar el alto de nuestra figura.
        '''
        self.ancho = ancho
        self.alto = alto
    @abstractmethod
    def area(self):
        '''
        Método vacío, que tiene el decorador "@abstractmethod", el cual 
        lo hace un método abstracto. Servirá más adelante para poder calcular el 
        área de los rectángulos que querramos.
        '''
        pass
class Rectangulo(Figura): 
    '''
    Se crea una clase hija, que hereda métodos y atributos de nuestra clase 
    abstracta previamente formada.
    
    ----------
    Métodos:
    ----------
        __init__(self, base, altura): Método que construye los atributos de la clase.
        area(self): Método que recibe los atributos (base y altura), y con estos calcula 
                    el área del rectángulo.
    
    ----------
    Atributos:
    ----------
        base=int-> Variable que almacena el valor de la base del rectángulo.

        altura=int-> Variable que almacena el valor de la altura del rectángulo.
    '''
    def __init__(self, base, altura):
        '''
        Método que construye los atributos de la clase.

        -----------
        Parámetros:
        -----------
            base=int-> Variable que almacena el valor de la base del rectángulo.

            altura=int-> Variable que almacena el valor de la altura del rectángulo.
        '''
        self.base = base
        self.altura = altura
    def area(self):
        '''
        Método que recibe los atributos (base y altura), y con estos calcula 
        el área del rectángulo.

        Retorna-> El area del rectángulo, lo hace debido que recibe los parámetros 
                  "base" y "altura"
        '''
        area=(self.base*self.altura)
        return(area)

class Tablero(Rectangulo):
    '''
    Clase hija de la Clase "Rectangulo", hereda los atributos 
    y los métodos de la super clase. Esta clase se la crea 
    con el objetivo de crear una base para colocar rectángulos
    dentro de ella.

    ----------
    Métodos:
    ----------

        __init__(self, rectangulo): Construye el atributo de la clase.

        rectangulo(self): Método que permite obtener el valor del rectángulo,
                          se utiliza el decorador property para darle el sentido 
                          de un get (obtener).

        rectangulo(self, value): Método que permite asignar el valor a nuestro rectángulo,
                                 se utiliza el decorador setter para aplicar el sentido de 
                                 encapsulamiento.

        calcularArea(self): Método que permite calcular finalmente el área del rectángulo.

    -----------
    Atributos:
    -----------
        rectangulo=int-> Variable que almacena el número de rectángulos.                             

    '''
    def __init__(self, rectangulo):
        '''
        Método que construye el atributo de la clase.

        -----------
        Parámetros:
        -----------
            rectangulo=int-> Variable que almacena el número de rectángulos.    

        '''
        self.rectangulo = rectangulo
    @property
    def rectangulo(self):
        '''
        Método que permite obtener el valor del rectángulo,
        se utiliza el decorador property para darle el sentido 
        de un get (obtener).

        Retorna-> El valor del rectángulo.
        '''
        return self._rectangulo
    @rectangulo.setter
    def rectangulo(self, value):
        '''
        Método que permite asignar el valor a nuestro rectángulo,
        se utiliza el decorador setter para aplicar el sentido de 
        encapsulamiento.
        '''
        self._rectangulo=value
    def calcularArea(self):
        '''
        Método que permite calcular finalmente el área del rectángulo.
        Y suma todas las áreas si desea calcular más de un rectángulo.
        '''
        area=0
        for i in range(self.rectangulo):            
            print("Se calculó el área del rectángulo " , str(i+1), " y fue:",rectanguloNuevo.area())
            area=area+rectanguloNuevo.area()
        print("El área total de los rectángulos es:",area)
if __name__=="__main__":
    '''
    Se pide los respectivos datos, en este caso será la base 
    y la altura de un rectángulo. Con esto se hace el programa
    dinámico.
    '''
    base=int(input("Ingrese la base del rectángulo: "))
    altura=int(input("Ingrese la altura de su rectángulo: "))
    '''
    Se instancia el objeto de tipo Rectangulo, de manera dinámica, se lo
    hace con los datos pedidos previamente.
    '''
    rectanguloNuevo=Rectangulo(base,altura)
    '''
    Se pide el número de rectángulos que se desea calcular el área.
    '''
    cantidadRectangulos=int(input("Ingrese la cantidad de rectángulos: "))
    '''
    Se instancia el objeto de tipo Tablero, con la cantidad previamente 
    ingresada por el usuario.
    '''
    tablero=Tablero(cantidadRectangulos)
    '''
    Se llama al método para calcular el área de cada rectángulo y 
    el área total.
    '''
    tablero.calcularArea()
    
