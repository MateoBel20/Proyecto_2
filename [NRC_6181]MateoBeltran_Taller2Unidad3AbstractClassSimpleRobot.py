'''
Se importa la clase abstracta ABC, la cual obliga 
a las subclases a implementar todos los métodos 
abstractos que se necesiten.
'''
from abc import ABC, abstractmethod
'''
    Se crean una clase padre, "Robot", la cual es una 
    clase abstracta (hereda ABC). La cual tiene tres subclases 
    o clases hija las cuales son "robotProgramacion", "robotCalculo", "robotEDO".

    ----------
    Métodos:
    ----------
        hacer(action): Método que le da la acción a la clase abstracta,
        en este caso la acción será dar las respectivas notas de un estudiante.
'''
class Robot(ABC):
    '''
    Clase padre abstracta que tiene como decorador el método 
    abstract, el cual le da la acción de dar notas.
    
    ------------
    Métodos:
    ------------
    hacer(action): Método que le da la acción a la clase abstracta,
    en este caso la acción será dar las respectivas notas de un estudiante.

    -----------
    Atributos:
    -----------
        action: Variable que almacena la acción de dar las respectivas notas.
    '''
    @abstractmethod
    def hacer(self,action):
        '''
        Método que le da la acción a la clase abstracta,
        en este caso la acción será dar las notas al estudiante.

        -----------
        Parámetros:
        -----------
            action: Variable que almacena la acción de dar las respectivas notas.
        '''
        pass

class robotProgramacion(Robot):
    '''
    Clase "robotProgramacion" es una subclase o clase hija de la 
    clase abstracta "Robot".

    ---------
    Métodos:
    ---------
       def hacer(self,action,notas): Método que permite dar las notas al respectivo estudiante
                                     de la materia de Programación.

    ----------
    Atributos:
    ----------
        action: Variable que almacena la acción de dar las respectivas notas.
        notas= Variable que almacena la nota del estudiante.
    '''
    def hacer(self,action,notas):
        '''
         Método que permite dar las notas al respectivo estudiante
        de la materia de Programación.

        ----------
        Parámetros:
        ----------
            action: Variable que almacena la acción de dar las respectivas notas.
            notas= Variable que almacena la nota del estudiante.
        '''
        print(f"El robot de la materia de POO {action} {notas} su promedio general ")

class robotCalculo(Robot):
    '''
    Clase "robotCalculo" es una subclase o clase hija de la 
    clase abstracta "Robot".

    ---------
    Métodos:
    ---------
       def hacer(self,action,notas): Método que permite dar las notas al respectivo estudiante
                                     de la materia de Cálculo Vectorial.

    ----------
    Atributos:
    ----------
        action: Variable que almacena la acción de dar las respectivas notas.
        notas= Variable que almacena la nota del estudiante.
    '''
    def hacer(self,action,notas):
        '''
         Método que permite dar las notas al respectivo estudiante
        de la materia de Cálculo Vectorial.

        ----------
        Parámetros:
        ----------
            action: Variable que almacena la acción de dar las respectivas notas.
            notas= Variable que almacena la nota del estudiante.
        '''
        print(f"El robot de la materia de Cálculo Vectorial {action} {notas} su promedio general ")

class robotEDO(Robot):
    '''
    Clase "robotEDO" es una subclase o clase hija de la 
    clase abstracta "Robot".

    ---------
    Métodos:
    ---------
       def hacer(self,action,notas): Método que permite dar las notas al respectivo estudiante
                                     de la materia de EDO.

    ----------
    Atributos:
    ----------
        action: Variable que almacena la acción de dar las respectivas notas.
        notas= Variable que almacena la nota del estudiante.
    '''
    def hacer(self,action,notas):
        '''
         Método que permite dar las notas al respectivo estudiante
        de la materia de EDO.

        ----------
        Parámetros:
        ----------
            action: Variable que almacena la acción de dar las respectivas notas.
            notas= Variable que almacena la nota del estudiante.
        '''
        print(f"El robot de la materia de EDO {action} {notas} su promedio general ")
        
if __name__=="__main__":
    '''
    Se crea una lista con las respectivas subclases, con las mismas,
    se podrá observar las diferentes notas del estudiante de cada materia.
    '''
    materia=[robotProgramacion(),robotCalculo(),robotEDO()]
    '''
    Para cada materia que exista en la la universidad ESPE, se darán notas
    al estudiante.
    '''
    for espe in materia:
        espe.hacer(action="calificó con  ",notas=" 18")

