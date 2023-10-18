'''
Se creó dos clases, la clase Persona es la encargada 
de administrar la propiedad de la persona, y la otra 
clase que se creó es la clase PersonaDB, la cual se encarga
de almacenar el datos de la persona.
'''
'''

'''
class Persona:
    '''
    La clase persona tiene dos métodos los cuales son el 
    construcutor y el otro método es el que se encarga de 
    administrar la propiedad de la persona.

    ----------
    Atributos:
    ----------
        nombre:str
                Variable que almacena el nombre de la persona.

    --------
    Métodos:
    --------    
        _init_(self,nombre):Construye los atributos de la clase.
        _repr_(self): Administra la propiedad de la persona.
    '''
    def _init_(self,nombre):
        '''
        _init_(self,nombre):
        Método que construye los atributos de la clase.

        -----------
        Parámetros:
        -----------
            nombre:str
                Variable que almacena el nombre de la persona.

        '''
        self.nombre = nombre

    def _repr_(self):
        '''
        Método que administra la propiedad de la persona.
        _repr_(self): Función que retorna el nombre de la persona.
        Returna el nombre de la persona.
        '''
        return f'Persona(nombre={self.nombre})'

'''

'''

class PersonDB:
    '''
    Clase que se encarga de almacenar a la persona en una base de datos.

    -----------
    Atributos:
    -----------
        persona:str
                Variable que almacena a la persona que se va a guardar en 
                la base de datos.

    ---------
    Métodos:
    --------
    save(self, persona): Método que almacena a la persona en una base de datos.
    '''
    def save(self, persona):
        '''
        Método que se encarga de almacenar a la persona en una base 
        de datos.

        ------------
        Parámetros:
        ------------
        persona:str
                Variable que almacena a la persona que se va a guardar en 
                la base de datos.
        '''
        print(f'Guarda a la {persona} en la base de datos')




if __name__ == '__main__:':
    '''
    Función principal que llama a todos los métodos para poder 
    ejecutar lo que se pide.
    '''
    '''
    Instancia de la variable de tipo Persona.
    '''
    ciudadano=Persona('Mateo Beltran')
    '''
    Nuestra base de datos, que contendrá la información 
    de nuestra persona.
    '''
    db=PersonDB()
    '''
    Función que permite guardar a la variable persona.
    '''
    db.save(ciudadano)