class Rectangle():
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



class tablero(Rectangle):
    @property
    def rectangles(self):      
        return self._rectangles

    @rectangles.setter
    def rectangles(self, value):     
        self._rectangles = value  

    def calculateArea(self):      
        area = 0
        for i in range(self.rectangles):
            area += figura.get_height()*figura.get_width()
        return area



if __name__=="__main__":
    valorAltura=int(input("Ingresar la altura del rectangulo: "))

    valorAncho=int(input("Ingresar el ancho del rectangulo: "))  

    figura=Rectangle(valorAltura,valorAncho)

    figurasEnTablero=tablero(valorAltura,valorAncho)  

    figurasEnTablero.rectangles=int(input("Ingresar la cantidad de los rectangulos para sumar todas las areas: "))
 
    print("Area total calculada: ",figurasEnTablero.calculateArea())