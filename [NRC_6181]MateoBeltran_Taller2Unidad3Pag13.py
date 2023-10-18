'''
Se importa la clase abstracta ABC, la cual obliga 
a las subclases a implementar todos los métodos 
abstractos que se necesiten.
'''
from abc import ABC, abstractmethod
'''
Se crean una clase padre, "Animal", la cual es una 
clase abstracta (hereda ABC). La cual tiene tres subclases 
o clases hija las cuales son "Lion", "Panda", "Snake"

----------
Métodos:
----------
    do(action): Método que le da la acción a la clase abstracta,
    en este caso la acción será alimentar al alimentar a los animales.
'''
class Animal(ABC):
    '''
    Clase padre abstracta que tiene como decorador el método 
    abstract, el cual le da la acción de alimentar.
    
    ------------
    Métodos:
    ------------
    do(action): Método que le da la acción a la clase abstracta,
    en este caso la acción será alimentar al alimentar a los animales.

    -----------
    Atributos:
    -----------
        action: Variable que almacena la acción de alimentar a los animales.
    '''
    @abstractmethod
    def do(self,action):
        '''
        Método que le da la acción a la clase abstracta,
        en este caso la acción será alimentar al alimentar a los animales.

        -----------
        Parámetros:
        -----------
            action: Variable que almacena la acción de alimentar a los animales.
        '''
        pass
class Lion(Animal):
    '''
    Clase "Lion" es una subclase o clase hija de la 
    clase abstracta "Animal".

    ---------
    Métodos:
    ---------
       def do(self,action,time): Método que permite alimentar en un respectivo tiempo 
       a los animales.

    ----------
    Atributos:
    ----------
        action: Variable que almacena la acción de alimentar a los animales.
        time: Variabel que almacena la hora que le corresponde ser alimentado
        al respectivo animal.


    '''
    def do(self,action,time):
        '''

        Método que le da la acción a la clase abstracta,
        en este caso la acción será alimentar al alimentar a los animales.

        -----------
        Parámetros:
        -----------
            action: Variable que almacena la acción de alimentar a los animales.
            time: Variabel que almacena la hora que le corresponde ser alimentado
                  al respectivo animal.
        '''
        print(f"{action} a lion! At {time}")
class Panda(Animal):
    '''
    Clase "Panda" es una subclase o clase hija de la 
    clase abstracta "Animal".

    ---------
    Métodos:
    ---------
       def do(self,action,time): Método que permite alimentar en un respectivo tiempo 
       a los animales.

    ----------
    Atributos:
    ----------
        action: Variable que almacena la acción de alimentar a los animales.
        time: Variabel que almacena la hora que le corresponde ser alimentado
        al respectivo animal.

    Al final da un mensaje, el cual está conformado por el parámetro
    "action" y el parámetro "time".
    '''
    def do(self,action,time):
        '''

        Método que le da la acción a la clase abstracta,
        en este caso la acción será alimentar al alimentar a los animales.

        -----------
        Parámetros:
        -----------
            action: Variable que almacena la acción de alimentar a los animales.
            time: Variabel que almacena la hora que le corresponde ser alimentado
                  al respectivo animal.
        
        Al final da un mensaje, el cual está conformado por el parámetro
        "action" y el parámetro "time".
        '''
        print(f"{action} a panda! At {time}")
class Snake(Animal):
    '''
    Clase "Snake" es una subclase o clase hija de la 
    clase abstracta "Animal".

    ---------
    Métodos:
    ---------
       def do(self,action,time): Método que permite alimentar en un respectivo tiempo 
       a los animales.

    ----------
    Atributos:
    ----------
        action: Variable que almacena la acción de alimentar a los animales.
        time: Variabel que almacena la hora que le corresponde ser alimentado
        al respectivo animal.

    Al final da un mensaje, el cual está conformado por el parámetro
    "action" y el parámetro "time".
    '''
    def do(self,action,time):
        '''

        Método que le da la acción a la clase abstracta,
        en este caso la acción será alimentar al alimentar a los animales.

        -----------
        Parámetros:
        -----------
            action: Variable que almacena la acción de alimentar a los animales.
            time: Variabel que almacena la hora que le corresponde ser alimentado
                  al respectivo animal.
        
        Al final da un mensaje, el cual está conformado por el parámetro
        "action" y el parámetro "time".
        '''
        print(f"{action} a snake! At {time}")
if __name__=="__main__":
    '''
    Función principal, en ella se realiza una lista de 
    los respectivos animales (clases hijas) que se necesitan alimentar.
    '''
    zoo=[Lion(),Panda(),Snake()]
    '''
    Ciclo for para imprimir las respectivas comidas y los respectivos 
    los respectivos horarios de cada alimentación.
    '''
    for animal in zoo:
        animal.do(action="feeding",time="10:10 PM")