'''
Se importa la clase abstracta ABC, la cual obliga 
a las subclases a implementar todos los métodos 
abstractos que se necesiten.
'''
from abc import ABC, abstractmethod
class Robot(ABC):
    '''
    Se crea una clase abstracta padre denominada "Robot", 
    la cual se tiene métodos para obtener las propiedades del objeto
    y tiene un método setter para dar las las propiedades del respectivo
    objeto.

    --------
    Métodos:
    --------
        espe_materia(self): Método que permite obtener la propiedad, 
                          en este caso será la materia que dispone la universidad ESPE. 
                          Se usa el decorador "property".
        espe_materia(self,espe): Método que va a permitir dar el tema 
                                 que se estudiará.Se utiliza el decorador "setter".
        tema(self):Método que se encarga de darle el tema al estudiante, se 
                   utiliza el decorador abstracto "abstractmethod". El respectivo decorador
                   convierte al método en un método abstracto.
        clases(self,parcial): Método que utiliza el decorador "abstractmethod", con esto el método 
                              se transforma en un método abstracto. Se encarga de brindar si se puede 
                              o no dar el respectivo tema en el parcial que se está cursando.
    -----------
    Atributos:
    -----------
        espe: Variable que va a almacenar la materia.
        parcial: Variable que almacena el respectivo parcial que se va a cursar.

    '''
    @property
    def espe_materia(self):
        '''
        Método que permite obtener la propiedad, 
        en este caso será la materia que dispone la universidad ESPE. 
        Se usa el decorador "property".

        Retorna la respectiva materia
        '''
        return self._espe

    @espe_materia.setter
    def espe_materia(self,espe):
        '''
        Método que va a permitir dar el tema 
        que se estudiará.Se utiliza el decorador "setter".
        Si no cumple con el parcial, no se podrá dar el 
        tema en la clase.
        '''
        if espe in self.tema:
            self._espe=espe
        else:
            raise ValueError("No se puede dar ese tema, porque no coincide con el parcial {espe}. ")

    @property
    @abstractmethod
    def tema(self):
        '''
        Método que se encarga de darle el tema al estudiante, se 
        utiliza el decorador abstracto "abstractmethod". El respectivo decorador
        convierte al método en un método abstracto.
        '''
        pass

    @abstractmethod
    def clases(self,parcial):
        '''
        Método que utiliza el decorador "abstractmethod", con esto el método 
        se transforma en un método abstracto. Se encarga de brindar si se puede 
        o no dar el respectivo tema en el parcial que se está cursando.

        ----------
        Parámetros:
        -----------
            parcial: Variable que almacena el respectivo parcial que se va a cursar.
        '''
        pass

class robotCalculo(Robot):
    '''
    Clase hija de la clase padre "Robot".

    ----------
    Métodos:
    ----------
        tema(self):Método que se encarga de darle el tema al estudiante, se 
                   utiliza el decorador abstracto "abstractmethod". El respectivo decorador
                   convierte al método en un método abstracto.
        clases(self,parcial): Método que utiliza el decorador "abstractmethod", con esto el método 
                              se transforma en un método abstracto. Se encarga de brindar si se puede 
                              o no dar el respectivo tema en el parcial que se está cursando.

    ----------
    Atributos:
    ----------
        parcial: Variable que almacena el respectivo parcial que se va a cursar.
    '''
    @property
    def tema(self):
        '''
        Método que se encarga de darle el tema al estudiante, se 
        utiliza el decorador abstracto "abstractmethod". El respectivo decorador
        convierte al método en un método abstracto.

        Retorna la lista de los temas que se pueden dar en el parcial.
        '''
        return["Integral Doble", "Derivadas Parciales", "Continuidad"]

    def clases(self,parcial):
        '''
        Método que utiliza el decorador "abstractmethod", con esto el método 
        se transforma en un método abstracto. Se encarga de brindar si se puede 
        o no dar el respectivo tema en el parcial que se está cursando.
        '''
        print(f"Vamos a estudiar {self._espe}  {parcial}")

class robotProgramacion(Robot):
    '''
    Clase hija de la clase padre "Robot".

    ----------
    Métodos:
    ----------
        tema(self):Método que se encarga de darle el tema al estudiante, se 
                   utiliza el decorador abstracto "abstractmethod". El respectivo decorador
                   convierte al método en un método abstracto.
        clases(self,parcial): Método que utiliza el decorador "abstractmethod", con esto el método 
                              se transforma en un método abstracto. Se encarga de brindar si se puede 
                              o no dar el respectivo tema en el parcial que se está cursando.

    ----------
    Atributos:
    ----------
        parcial: Variable que almacena el respectivo parcial que se va a cursar.
    '''
    @property
    def tema(self):
        '''
        Método que se encarga de darle el tema al estudiante, se 
        utiliza el decorador abstracto "abstractmethod". El respectivo decorador
        convierte al método en un método abstracto.

        Retorna la lista de los temas que se pueden dar en el parcial.
        '''
        return["Interfaz Gráfica", "MONGO DB"]
    def clases(self,parcial):
        '''
        Método que utiliza el decorador "abstractmethod", con esto el método 
        se transforma en un método abstracto. Se encarga de brindar si se puede 
        o no dar el respectivo tema en el parcial que se está cursando.
        '''  
        print(f"Vamos a estudiar {self._espe} {parcial}")

if __name__=="__main__":
    '''
    Se instancia el respectivo objeto, en este caso es un
    objeto de tipo clase "robotCalculo".
    '''
    robot = robotCalculo()
    '''
    Se llama al método setter, para designar el respectivo 
    tema para el parcial. Si no se encuentra en la 
    lista previamente mostrada, automáticamente no 
    le permite dar el tema en el parcial.
    '''
    robot.espe_materia = "Derivadas Parciales" 
    '''
    Se llama al método "clases", el cual establece 
    el parcial que se va a dar.
    '''
    robot.clases("en el parcial uno")
    '''
    Se instancia el respectivo objeto, en este caso es un
    objeto de tipo clase "robotProgramacion".
    '''
    robotProgra = robotProgramacion  ()
    '''
    Se llama al método setter, para designar el respectivo 
    tema para el parcial. Si no se encuentra en la 
    lista previamente mostrada, automáticamente no 
    le permite dar el tema en el parcial.
    '''
    robotProgra.espe_materia = "MONGO DB"
    '''
    Se llama al método "clases", el cual establece 
    el parcial que se va a dar.
    '''
    robotProgra.clases("en el parcial dos")
