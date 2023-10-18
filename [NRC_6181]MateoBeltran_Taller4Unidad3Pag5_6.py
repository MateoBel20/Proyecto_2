import math

class ShapeMeta(type):
    '''
    Se declara la clase "ShapeMeta", para poder 
    utilizar las funciones de una clase.
    Si la subclase "area" esta presente se llama a la misma

    ------------
    Métodos:
    ------------
    
    __instancecheck__(self, instance): Devuelve True si la instancia es un objeto de clase instanciado directa o indirectamente.
    __subclasscheck__(self, subclass):Agrupa datos y funcionalidad juntos. Proporciona todas las características del objeto con cual se va trabajar.
    '''
    def __instancecheck__(self, instance):
        '''
        Devuelve True si la instancia es un objeto de clase 
        instanciado directa o indirectamente.

        --------
        Retorna:
        --------
            Verdadero si la instancia del objeto está correctamente instanciado con la clase.
        '''
        return self.__subclasscheck__(type(instance))

    def __subclasscheck__(self, subclass):
        '''
        Agrupa datos y funcionalidad juntos. Proporciona todas las 
        características del objeto con cual se va trabajar.

        ---------
        Retorna:
        ---------
            Retorna las diferes características, en este 
            caso será el área.
        '''
        return (hasattr(subclass, 'area') and
        callable(subclass.area))

class ShapeInterface(metaclass=ShapeMeta):
    '''
    Clase vacía, la cual es clase hija de ShapeMeta
    '''
    pass

class Triangulo(ShapeInterface):
    '''
    Clase Triangulo, obtiene y da los valores respectivos 
    para sacar el área de la misma figura.

    ------------
    Métodos:
    ------------
        __init__(self, baseTriangulo, alturaTriangulo): Construye los atributos de la clase.
        get_baseTriangulo(self): Obtiene el valor de la base de la triángulo.
        set_baseTriangulo(self, baseTriangulo): Establece el valor de la base del triángulo.
        get_alturaTriangulo(self): Obtiene el valor de la altura de la triángulo.
        set_alturaTriangulo(self, alturaTriangulo): Establece el valor de la altura del triángulo.
        area(self): Método que retorna el área del triángulo.
    
    ----------
    Atributos:
    ----------

        baseTriangulo: Variable que va almacenar la base del triángulo.
        alturaTriangulo: Variable que va almacenar la altura del triángulo.
    '''
    def __init__(self, baseTriangulo, alturaTriangulo):
        '''
        Construye los atributos de la clase.

        -----------
        Parámetros:
        -----------
            baseTriangulo: Variable que va almacenar la base del triángulo.

            alturaTriangulo: Variable que va almacenar la altura del triángulo.
        '''
        self._baseTriangulo = baseTriangulo
        self._alturaTriangulo= alturaTriangulo

    def get_baseTriangulo(self):
        '''
        Obtiene el valor de la base de la triángulo.

        Retorna: El valor de la base del triángulo.
        '''
        return self._baseTriangulo

    def set_baseTriangulo(self, baseTriangulo):
        '''
        Establece el valor de la base del triángulo.

        -----------
        Parámetros:
        -----------
            baseTriangulo: Variable que va almacenar la base del triángulo.
        '''
        self._baseTriangulo = baseTriangulo

    def get_alturaTriangulo(self):
        '''
        Obtiene el valor de la altura de la triángulo.

        Retorna: Altura del triángulo
        '''
        return self._alturaTriangulo

    def set_alturaTriangulo(self, alturaTriangulo):
        '''
        Establece el valor de la altura del triángulo.
        '''
        self._alturaTriangulo = alturaTriangulo


    def area(self):
        '''
        Método que retorna el área del triángulo.

        Retorna: El área del triángulo.
        '''
        return (self.get_baseTriangulo() * self.get_alturaTriangulo())/2




class Circulo(ShapeInterface):
    '''
    Clase circulo, obtiene y da los valores respectivos 
    para sacar el área de la misma figura.

    --------
    Métodos:
    --------
        __init__(self, radio):Construye los atributos de la clase.
        get_radio(self):Obtiene el valor del radio del círculo.
        set_radio(self, radio): Establece el valor del radio del círculo.
        area(self): Método que retorna el área del círculo.

    ----------
    Atributos:
    ----------
        radio: Variable que almacena el valor del radio de la circunferencia.
    '''
    def __init__(self, radio):
        '''
        Construye los atributos de la clase.

        -----------
        Parámetros:
        -----------
            radio: Variable que almacena el valor del radio de la circunferencia.
        '''
        self._radio = radio

    def get_radio(self):
        '''
        Obtiene el valor del radio del círculo.

        Retorna: El valor del radio.
        '''
        return self._radio

    def set_radio(self, radio):
        '''
        Establece el valor del radio del círculo.

        -----------
        Parámetros:
        -----------

        '''
        self._radio = radio

    def area(self):
        '''
        Método que retorna el área del círculo.

        Retorna: Área del círculo.
        '''
        return self.get_radio() * self.get_radio() * math.pi


class Rombo(ShapeInterface):
    '''
    Clase rombo, obtiene y da los valores respectivos 
    para sacar el área de la misma figura.

    -----------
    Métodos:
    -----------
        __init__(self, diagonalMayor, diagonalMenor): Construye los atributos de la clase.
        get_diagonalMayor(self):Obtiene el valor de la diagonal mayor.
        set_diagonalMayor(self, diagonalMayor): Establece el valor de la diagonal mayor.
        get_diagonalMenor(self):Obtiene el valor de la diagonal menor.
        set_diagonalMenor(self, diagonalMenor): Establece el valor de la diagonal menor.
        area(self): Método que retorna el área del rombo.

    -----------
    Atributos:
    -----------
        diagonalMayor: Variable que va almacenar el valor de la digonal mayor.
        diagonalMenor: Variable que va almacenar el valor de la digonal menor.
    '''
    def __init__(self, diagonalMayor, diagonalMenor):
        '''
        Construye los atributos de la clase.

        -----------
        Parámetros:
        -----------
            diagonalMayor: Variable que va almacenar el valor de la digonal mayor.
            diagonalMenor: Variable que va almacenar el valor de la digonal menor.

        '''
        self._diagonalMayor = diagonalMayor
        self._diagonalMenor = diagonalMenor
        
    def get_diagonalMayor(self):
        '''
        Obtiene el valor de la diagonal mayor.

        Retorna: Valor del diagonal mayor.
        '''
        return self._diagonalMayor

    def set_diagonalMayor(self, diagonalMayor):
        '''
        Establece el valor de la diagonal mayor.

        -----------
        Parámetros:
        -----------
            diagonalMayor: Variable que va almacenar el valor de la digonal mayor.
        '''
        self._diagonalMayor = diagonalMayor 

    def get_diagonalMenor(self):
        '''
        Obtiene el valor de la diagonal menor.

        Retorna: Valor de la diagonal menor.
        '''
        return self._diagonalMenor

    def set_diagonalMenor(self, diagonalMenor):
        '''
        Establece el valor de la diagonal menor.
        '''
        self._diagonalMenor = diagonalMenor

    
    def area(self):
        '''
        Método que retorna el área del rombo.
        '''
        return (self.get_diagonalMayor() *self.get_diagonalMenor()  )/2


class Cuadrado(ShapeInterface):
    '''
    Clase cuadrado, obtiene y da los valores respectivos 
    para sacar el área de la misma figura.

    --------------
    Métodos:
    --------------
        __init__(self, ladosCuadrado): Construye los atributos de la clase.
        get_ladosCuadrado(self):Obtiene el valor del lado del cuadrado.
        set_ladosCuadrado(self, ladosCuadrado): Establece el valor del lado del cuadrado.
        area(self): Retorna el área del cuadrado.

    -----------
    Atributos:
    -----------
        ladosCuadrado: Variable que almacena la medida del lado del cuadrado.
    '''
    def __init__(self, ladosCuadrado):
        '''
        Construye los atributos de la clase.

        -----------
        Parámteros:
        -----------
            ladosCuadrado: Variable que almacena la medida del lado del cuadrado.
        '''
        self._ladosCuadrado = ladosCuadrado

    def get_ladosCuadrado(self):
        '''
        Obtiene el valor del lado del cuadrado.
        
        Retorna: La medida del lado del cuadrado.
        '''
        return self._ladosCuadrado

    def set_ladosCuadrado(self, ladosCuadrado):
        '''
        Establece el valor del lado del cuadrado.
        '''
        self._ladosCuadrado = ladosCuadrado

    def area(self):
        '''
        Método que retorna el área del cuadrado.
        '''
        return self.get_ladosCuadrado() * self.get_ladosCuadrado()



class Rectangulo(ShapeInterface):
    '''
    Clase rectángulo, obtiene y da los valores respectivos 
    para sacar el área de la misma figura.

    -----------
    Métodos:
    ----------- 
        __init__(self, ancho, alto):Construye los atributos de la clase.
        get_ancho(self): Obtiene el valor del ancho del rectángulo.
        set_ancho(self, ancho): Establece el valor del ancho del rectángulo.
        get_alto(self):Obtiene el valor de la altura del rectángulo.
        set_alto(self, alto):Establece el valor de la altura del rectángulo.
        area(self):

    -----------
    Atributos:
    -----------
        ancho: Variable que almacena el ancho del rectángulo.
        alto: Variable que almacena la altura del rectángulo.
    '''
    def __init__(self, ancho, alto):
        '''
        Construye los atributos de la clase.
        
        -----------
        Parámetros:
        -----------
           ancho: Variable que almacena el ancho del rectángulo.
           alto: Variable que almacena la altura del rectángulo. 
        '''
        self._ancho= ancho
        self._alto = alto

    def get_ancho(self):
        '''
        Obtiene el valor del ancho del rectángulo.

        Retorna el valor del ancho del rectángulo.
        '''
        return self._ancho

    def set_ancho(self, ancho):
        '''
        Establece el valor del ancho del rectángulo.
        '''
        self._ancho = ancho

    def get_alto(self):
        '''
        Obtiene el valor de la altura del rectángulo.

        Retorna la altura del rectángulo.
        '''
        return self._alto

    def set_alto(self, alto):
        '''
        Establece el valor de la altura del rectángulo.
        '''
        self._height = alto

    def area(self):
        '''
        Área del rectángulo.
        '''
        return self.get_ancho() * self.get_alto()


class tablero():
    '''
    Clase para poder graficar las figuras.

    ----------
    Métodos:
    ----------
        __init__(self,formas): Construye los atributos de la clase.
        calculateArea(self): Calcula el área total.

    -----------
    Atributos:
    -----------

        formas: Variable que almacena las figuras.
    '''
    def __init__(self,formas):
        '''
        Construye los atributos de la clase.
        '''
        self._formas=formas

    def calculateArea(self):
        '''
        Calcula el área total.
        '''
        area=0

        for formas in self._formas:
            area+=formas.area()
        return area


'''Función principal'''
if __name__=="__main__":
    ''''
    Menú principal que consta con 5 figuras, el usuario elige cual quiere dibujar.
    '''
    print("-.-.-.-.-.-.-.-.-.-.-.- \n Menu Principal: \n-.-.-.-.-.-.-.-.-.-.-.-")
    print("\n 1- Triangulo")
    print("\n 2- Círculo")
    print("\n 3- Cuadrado")
    print("\n 4- Rombo ")
    print("\n 5- Rectángulo")
    print("-.-.-.-.-.-.-.-.-.-.-.-")
    '''
    Número de figuras
    '''
    numeroDeFiguras=int(input("\n¿Cuántas figuras desea poner en el tablero?: "))
    '''
    Lita que va almacenar las diferentes figuras.
    '''
    lista=[]
    '''
    Se inicializa los números en verdadero.
    '''
    numeros=True
    
    if numeroDeFiguras<7 and numeroDeFiguras>0:
        '''
        Condición que permite darle al usuario una serie de figuras
        las cuales no puede superarse de 7, son las figuras que se 
        presentan en el menú.
        '''
        while numeros == True:
                for i in range(numeroDeFiguras):
                    figurasSeleccionadas=int(input("Ingrese el/los números que corresponden a cada figura: "))
                    lista.append(figurasSeleccionadas)

                numeros=False

    listaFiguras=[]
    '''
    Lista que se va almacenar las diferentes figuras que decida el usuario.
    '''
    print("       ")
    
    if 1 in lista:
        '''
        Se pide los datos para sacar el área del triángulo, 
        se lo hace para instanciar de manera dinámica.
        '''
        alturaTriangulo=float(input("Ingrese valor altura del triángulo: "))
        basetriangulo=float(input("Ingrese valor base del triángulo: "))
        '''
        Se instancia el objeto de tipo Triangulo, de manera dinámica.
        '''
        triangulo=Triangulo(basetriangulo,alturaTriangulo)
        '''
        Se llama al método que calcula el área.
        '''
        print("Área total calculada del triángulo: ",triangulo.area())
        '''
        Se agraga la figura a la lista.
        '''
        listaFiguras.append(triangulo)
        print("\n")

        

    if 2 in lista:
        '''
        Se pide los datos para sacar el área del circunferencia, 
        se lo hace para instanciar de manera dinámica.
        '''
        
        radio=float(input("Ingrese el radio de la circunferencia: "))
        '''
        Se instancia el objeto de tipo Circulo, de manera dinámica.
        '''
        circunferencia=Circulo(radio)
        '''
        Se llama al método que calcula el área.
        '''
        print("Área de la circunferencia: ",circunferencia.area())
        '''
        Se agraga la figura a la lista.
        '''
        listaFiguras.append(circunferencia)
        print("\n") 

    if 3 in lista:
        '''
        Se pide los datos para sacar el área del cuadrado, 
        se lo hace para instanciar de manera dinámica.
        '''

        medidaDeLados=int(input("Ingrese la medida del lado del cuadrado: "))
        '''
        Se instancia el objeto de tipo Circulo, de manera dinámica.
        '''
        cuadrado=Cuadrado(medidaDeLados)
        '''
        Se llama al método que calcula el área.
        '''
        print("Área del cuadrado: ",cuadrado.area())
        '''
        Se agraga la figura a la lista.
        '''
        listaFiguras.append(cuadrado)
        print("\n")


        

    if 4 in lista:
        '''
        Se pide los datos para sacar el área del rombo, 
        se lo hace para instanciar de manera dinámica.
        '''
        diagonalMayor=float(input("Ingrese valor de diagonal mayor del rombo: "))
        diagonalMenor=float(input("Ingrese valor de diagonal menor del rombo: "))
        '''
        Se instancia el objeto de tipo Circulo, de manera dinámica.
        '''
        rombo=Rombo(diagonalMayor,diagonalMenor)
        '''
        Se llama al método que calcula el área.
        '''
        print("Área del rombo: ",rombo.area())
        '''
        Se agraga la figura a la lista.
        '''
        listaFiguras.append(rombo)
        print("\n")
        
    if 5 in lista:
        '''
        Se pide los datos para sacar el área del rectángulo, 
        se lo hace para instanciar de manera dinámica.
        '''
        alturaRectangulo=int(input("Ingresar la altura del rectángulo: "))
        anchoRectangulo=int(input("Ingresar el ancho del rectangulo: "))
 
        '''
        Se instancia el objeto de tipo Circulo, de manera dinámica.
        '''
        
        rectangulo=Rectangulo(alturaRectangulo,anchoRectangulo)
        '''
        Se llama al método que calcula el área.
        '''
        print("Área del rectángulo: ",rectangulo.area())
        '''
        Se agraga la figura a la lista.
        '''
        listaFiguras.append(rectangulo)
        print("\n")

        
    else:
        print("SOBREPASO EL LÍMITE DE FIGURAS")



    '''Se instancia el objeto table, con la lista de las figuras'''
    valorTablero=tablero(listaFiguras)

    '''Se llama al método para calcular el total de las áreas'''
    print("shape calculado final total: ",valorTablero.calculateArea())