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


    
class Person:
    '''
    La clase Person se encarga de ser fachada de la clase PersonDB.


    ----------
    Atributos:
    ----------
        name: str
            Variable que almacena el nombre de la persona.


    ---------
    Métodos:
    ---------
       _init_(self,name):Construye los atributos de la clase.
       _repr_(self): Administra la propiedad de la persona.
       save(self):Método que almacena a la persona en una base de datos.

    
    '''
    def _init_(self,name):
        '''
        Método que construye los atributos de la clase.
            _init_(self,name):Construye los atributos de la clase.
        '''
        self.name = name
        self.db = PersonDB()

    def _repr_(self):
        '''
        Método que administra la proiedad de la persona.
            _repr_(self): Administra la propiedad de la persona.
            Returna el nombre de la persona.
        '''
        return f'Person(name={self.name})'

    def save(self):
        '''
        Método de fachada que permite guardar a la persona en la base de datos.

            save(self):Método que almacena a la persona en una base de datos.
        '''
        self.db.save(person=self)






if __name__ == '__main__':
    '''
    Función principal, en ella se llaman a todos los 
    métodos para poder ejecutar lo que se necesite.
    '''
    '''
    Instancia de la variable de tipo Person.
    '''
    ciudadano=Person('Valentin Guerrero')
    '''
    Se llama a la función save(), la cual permite 
    guardad al ciudadano en la base de datos.
    '''
    ciudadano.save()