class CuadrilateroMeta(type):
    '''
    Clase CuadrilateroMeta que es una interfaz, la cual
    se encarga internamente de separar a la figura, Rectángulo
    y a la figura Cuadrado. Con esta clase se garantiza que 
    cada la figura Cudrado y la figura Rectángulo sean responsables
    de cada uno de sus métodos y atributos.

    ----------
    Métodos:
    ----------
        __instancecheck__(self,instance):Método que devuelve "TRUE" si la instacia es un objeto de clase instanciado 
                                         directa o indirectamente (herencia). Para lograr eso, este método implementa 
                                         la función "instance".
        __subclasscheck__(self, subclass): Método que se encarga de devolver "TRUE" si la subclase hereda 
                                           los respectivos métodos y atributos de la clase padre.

    -----------
    Atributos:
    -----------
        instance: Variable que almacena la información de la instancia del objeto
                  perteneciente a la respectiva clase.
        subclass: Variable que almacena la respectiva información de la
                  subclase o clase hija.
    '''
                                         
                                
    def __instancecheck__(self,instance):
        '''
        Método que devuelve "TRUE" si la instacia es un objeto de clase instanciado 
        directa o indirectamente (herencia). Para lograr eso, este método implementa 
        la función "instance".

        -----------
        Parámetros:
        -----------
            instance: Variable que almacena la información de la instancia del objeto
                      perteneciente a la respectiva clase.

        RETORNA: La instancia del objeto.
        '''
        return self.__subclasscheck__(type(instance))

    def __subclasscheck__(self, subclass):
        '''
        Método que se encarga de devolver "TRUE" si la subclase hereda 
        los respectivos métodos y atributos de la clase padre.

        -----------
        Parámetros:
        -----------
            subclass: Variable que almacena la respectiva información de la
                      subclase o clase hija.

        RETORNA: Llama a las subclases que estén correctamente declaradas e instanciadas.
        '''
        return (hasattr(subclass,'area')and callable(subclass.area)) \
            and (hasattr(subclass,'get_height') and callable(subclass.get_height)) \
            and (hasattr(subclass,'get_width') and callable(subclass.get_width)) \
        

class InterfaceCuadrilatero(metaclass=CuadrilateroMeta):
    '''
    Clase vacía que se encarga de servir como 
    base para separar las figuras Rectángulo y Cuadrado.
    '''
    pass

class Rectangulo(InterfaceCuadrilatero):
    '''
    Clase rectángulo, obtiene y da los valores respectivos 
    para sacar el área de la misma figura. Clase hija de 
    la clase padre "InterfaceCuadrilatero"

    -----------
    Métodos:
    ----------- 
        __init__(self, ancho, altura):Construye los atributos de la clase.
        get_ancho(self): Obtiene el valor del ancho del rectángulo.
        set_ancho(self, ancho): Establece el valor del ancho del rectángulo.
        get_altura(self):Obtiene el valor de la altura del rectángulo.
        set_altura(self, alto):Establece el valor de la altura del rectángulo.
        area(self): Retorna el área de la figura.

    -----------
    Atributos:
    -----------
        ancho: Variable que almacena el ancho del rectángulo.
        alto: Variable que almacena la altura del rectángulo.
    '''
    def __init__(self, ancho, altura):
        '''
        Construye los atributos de la clase.
        
        -----------
        Parámetros:
        -----------
           ancho: Variable que almacena el ancho del rectángulo.
           altura: Variable que almacena la altura del rectángulo. 
        '''
        self._ancho = ancho
        self._altura = altura

    def get_ancho(self):
        '''
        Obtiene el valor del ancho del rectángulo.

        Retorna el valor del ancho del rectángulo.
        '''
        return self._ancho

    def set_ancho(self, ancho):
        '''
        Establece el valor del ancho del rectángulo.
        
        -----------
        Parámetros:
        -----------
            ancho: Variable que almacena el ancho del rectángulo.
        '''
        self._ancho = ancho

    def get_altura(self):
        '''
        Obtiene el valor de la altura del rectángulo.

        Retorna la altura del rectángulo.
        '''
        return self._altura

    def set_altura(self, altura):
        '''
        Establece el valor de la altura del rectángulo.

        -----------
        Parámetros:
        -----------
            altura:Variable que almacena la altura del rectángulo.
        '''
        self._altura = altura

    def area(self):
        '''
        Método que retorna el área del rectángulo.
        '''
        return self.get_ancho() * self.get_altura()

class Cuadrado(InterfaceCuadrilatero):
    '''
    Clase Cuadrado, obtiene y da los valores respectivos 
    para sacar el área de la misma figura. Clase hija de 
    la clase padre "InterfaceCuadrilatero".

    -----------
    Métodos:
    -----------
        __init__(self, ancho):Construye los atributos de la clase.
        get_ancho(self): Obtiene el valor del ancho del cuadrado.
        set_ancho(self, ancho): Establece el valor del ancho del cuadrado.
        get_altura(self):Obtiene el valor de la altura del cuadrado.
        set_altura(self, altura):Establece el valor de la altura del cuadrado.
        area(self): Retorna el área de la figura.

    -----------
    Atributos:
    -----------
        ancho: Variable que almacena el ancho del cuadrado.
        altura: Variable que almacena la altura del cuadrado. 
    '''
    def __init__(self, ancho):
        '''
        Construye los atributos de la clase.

        -----------
        Parámetros:
        -----------
            ancho: Variable que almacena el ancho del cuadrado.
        '''
        self._ancho = ancho
        self._altura = ancho

    def get_ancho(self):
        '''
        Obtiene el valor del ancho del cuadrado.

        RETORNA: El ancho del cuadrado.
        '''
        return self._ancho

    def set_ancho(self, ancho):
        '''
        Establece el valor del ancho del cuadrado.

        -----------
        Parámetros:
        -----------
           ancho: Variable que almacena el ancho del cuadrado. 
        '''
        self._ancho = ancho
        self._altura = ancho

    def get_altura(self):
        '''
        Obtiene el valor de la altura del cuadrado.

        RETORNA: Altura del cuadrado.
        '''   
        return self._altura

    def set_altura(self, altura):
        '''
        Establece el valor de la altura del cuadrado.

        ------------
        Parámetros:
        ------------
            altura: Variable que almacena la altura del cuadrado. 
        '''
        self._altura = altura
        self._ancho = altura
    
    def area(self):
        '''
        Método que retorna el área del cuadrado.
        '''
        return self.get_ancho() * self.get_altura()
        
if __name__ == '__main__':
    '''
    Se pide al usuario el número de figuras que desea
    calcular el área.
    '''
    numeroFiguras = int(input("Ingrese el número de cuadrados que desea: "))
    while (numeroFiguras < 0):
        '''
        Ciclo while para controlar la cantidad de figuras que ingrese 
        el usuario, si es algo ilógico, le volverá a pedir el 
        número de figuras.
    
        numeroFigura= Variable que almacena el número de figuras.
        '''
        print("Error, ingrese correctamente el número de figuras")
        numeroFiguras = int(input("Ingrese el número de cuadrados que desea: "))

    '''
    Para la suma total de las áreas de los cuadrados, la suma se 
    debe inicializar en cero.
    '''
    sumaTotal = 0
    for cantidad in range (numeroFiguras):
        '''
        Dependiendo del número de figuras que quiera el usuario
        se le pedirá la medida del lado de un cuadrado.
        La fórmula para calcular el área del es el lado elevado al cuadrado.

        medidaDeLado= Variable que almacenará la medida del lado del cuadrado.
        '''
        medidaDeLado=float(input("Ingresar la medidad del lado del cuadrado: "))
        '''
        Con la medida proporcionado por el usuario, se 
        instancia el objeto de manera dinámica.
        '''
        figura=Cuadrado(medidaDeLado)
        '''
        Se muestra el área de los cuadrados de manera individual.
        '''
        print("El área del cuadrado ""#",(cantidad+1)," es: ", figura.area())
        
        '''
        Se crea una variable almacenará las suma de todas las área de 
        los cuadrados que desee el usuario.
        '''
        sumaTotal += figura.area()
        '''
        Se muestra la suma total de las áreas correspondiente
        al número de figuras que ingresó el usuario.
        '''
    print("La suma de áreas de los cuadrados es: ",sumaTotal)
        