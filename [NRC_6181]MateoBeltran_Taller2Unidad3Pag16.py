'''
Se importa la clase abstracta ABC, la cual obliga 
a las subclases a implementar todos los métodos 
abstractos que se necesiten.
'''
from abc import ABC, abstractmethod
class Animal(ABC):
    '''
    Se crea una clase abstracta padre denominada "Animal", 
    la cual se tiene métodos para obtener las propiedades del objeto
    y tiene un método setter para dar las las propiedades del respectivo
    objeto.

    --------
    Métodos:
    --------
        food_eaten(self): Método que permite obtener la propiedad, 
                          en este caso será la comida para el respectivo animal. Se usa el 
                          decorador "property".
        food_eaten(self,food): Método que va a permitir dar la comida 
                               al respectivo animal. Se utiliza el decorador "setter".
        diet(self):Método que se encarga de darle la dieta a cada animal, se 
                   utiliza el decorador abstracto "abstractmethod". El respectivo decorador
                   convierte al método en un método abstracto.
        feed(self,time): Método que utiliza el decorador "abstractmethod", con esto el método 
                         se transforma en un método abstracto. Se encarga de brindar si se puede 
                         o no alimentar al respectivo animal.
    -----------
    Atributos:
    -----------
        food: Variable que va a almacenar la comida del animal.
        time: Variable que almacena la hora para alimentar al animal.

    '''
    @property
    def food_eaten(self):
        '''
        Método que permite obtener la propiedad, 
        en este caso será la comida para el respectivo animal. Se usa el 
        decorador "property".

        Retorna el alimento.
        '''
        return self._food

    @food_eaten.setter
    def food_eaten(self,food):
        '''
        Método que va a permitir dar la comida 
        al respectivo animal. Se utiliza el decorador "setter".
        Se utiliza un condicional para determinar si el alimento
        es correcto para el respectivo animal.

        -----------
        Parámetros:
        -----------
            food: Variable que va a almacenar la comida del animal.
        '''
        if food in self.diet:
            self._food=food
        else:
            raise ValueError("You can't feed this animal with {food}. ")

    @property
    @abstractmethod
    def diet(self):
        '''
        Método que se encarga de darle la dieta a cada animal, se 
        utiliza el decorador abstracto "abstractmethod". El respectivo decorador
        convierte al método en un método abstracto.
        '''
        pass

    @abstractmethod
    def feed(self,time):
        '''
        Método que utiliza el decorador "abstractmethod", con esto el método 
        se transforma en un método abstracto. Se encarga de brindar si se puede 
        o no alimentar al respectivo animal.

        -----------
        Parámetros:
        -----------
        time: Variable que almacena la hora para alimentar al animal.
        '''
        pass

class Lion(Animal):
    '''
    Clase hija de la clase padre "Animal".

    ----------
    Métodos:
    ----------
        diet(self):Método que se encarga de darle la dieta a cada animal, se 
                       utiliza el decorador abstracto "abstractmethod". El respectivo decorador
                       convierte al método en un método abstracto.
        
                       Retorna la lista de alimentos que puede comer el león.

        feed(self,time): Método que utiliza el decorador "abstractmethod", con esto el método 
                         se transforma en un método abstracto. Se encarga de brindar si se puede 
                         o no alimentar al respectivo animal.

    ----------
    Atributos:
    ----------
        time: Variable que almacena la hora para alimentar al animal.
    '''
    @property
    def diet(self):
        '''
        Método que se encarga de darle la dieta a cada animal, se 
        utiliza el decorador abstracto "abstractmethod". El respectivo decorador
        convierte al método en un método abstracto.


        Retorna la lista de alimentos que puede comer el león.

        '''
        return["antelope", "cheetah", "buffaice"]

    def feed(self,time):
        '''
        Método que utiliza el decorador "abstractmethod", con esto el método 
        se transforma en un método abstracto. Se encarga de brindar si se puede 
        o no alimentar al respectivo animal.

        -----------
        Parámetros:
        -----------
            time: Variable que almacena la hora para alimentar al animal.
        '''
        print(f"Feeding a lion with {self._food} meat! at {time}")

class Snake(Animal):
    '''
    Clase hija de la clase padre "Animal".
    ----------
    Métodos:
    ----------
        diet(self):Método que se encarga de darle la dieta a cada animal, se 
                       utiliza el decorador abstracto "abstractmethod". El respectivo decorador
                       convierte al método en un método abstracto.
        
                       Retorna la lista de alimentos que puede comer el león.

        feed(self,time): Método que utiliza el decorador "abstractmethod", con esto el método 
                         se transforma en un método abstracto. Se encarga de brindar si se puede 
                         o no alimentar al respectivo animal.

    '''
    @property
    def diet(self):
        '''
        Método que se encarga de darle la dieta a cada animal, se 
        utiliza el decorador abstracto "abstractmethod". El respectivo decorador
        convierte al método en un método abstracto.


        Retorna la lista de alimentos que puede comer el león.

        '''
        return["frog", "rabbit"]
    def feed(self,time):
        '''
        Método que utiliza el decorador "abstractmethod", con esto el método 
        se transforma en un método abstracto. Se encarga de brindar si se puede 
        o no alimentar al respectivo animal.

        -----------
        Parámetros:
        -----------
            time: Variable que almacena la hora para alimentar al animal.
        '''
        print(f"Feeding a snake with {self._food} meat! at {time}")

if __name__=="__main__":
    '''
    Se instancia el respectivo objeto, en este caso es un
    objeto de tipo clase "Lion".
    '''
    felino = Lion()
    '''
    Se llama al método setter, para designar el respectivo 
    alimento para el animal. Si no se encuentra en la 
    lista previamente mostrada, automáticamente no 
    le permite alimentar al animal.
    '''
    felino.food_eaten = "buffaice" 
    '''
    Se llama al método "feed", el cual establece 
    la hora exacta par alimentar al respectivo animal.
    '''
    felino.feed("9:30 AM")
    '''
    Se instancia el respectivo objeto, en este caso es un
    objeto de tipo clase "Snake".
    '''
    reptil = Snake()
    '''
    Se llama al método setter, para designar el respectivo 
    alimento para el animal. Si no se encuentra en la 
    lista previamente mostrada, automáticamente no 
    le permite alimentar al animal.
    '''
    reptil.food_eaten = "rabbit"
    '''
    Se llama al método "feed", el cual establece 
    la hora exacta par alimentar al respectivo animal.
    '''
    reptil.feed("11:45 AM")  