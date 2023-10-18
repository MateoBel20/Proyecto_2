'''
Se crea una clase que no aplica el principio de responsabilidad única 
y tiene dos objetivos administrar la propiedad de la persona 
y almacenar el nombre de la persona en una base de datos.

-----------------
Atributos:
-----------------
    nombre:str
            Variable que almacena el nombre de la persona.
-----------------
Métodos:
-----------------
    _init_(self,nombre): Construye el atributo de la clase
    _repr_(self):Función que administra la propiedad de la persona.
    save(cls, persona): Almacena a la persona en la base de datos. cuando me toque prorgramar podré utilizar el teclado de una mejor vez 
    no como ahora que no me sale tan rápido escribir si se puede programar con esto solo toca acostumbrarse nada más es mucho más grande uuuo
    confirmmaaaaaaaaaaaaaaaaaaaaaaaaa ahora mija  ya me sale más rápido la escritura mija mija mija mija dale dale dalqeu si se puedeeeeeeeeee
    ahora ahora ahora ahora ahora 
    
'''
class Person:

    def _init_(self,nombre):
        '''
        Método constructor de la clase.
        _init_(self,nombre): Construye el atributo de la clase.


        ------------
        Parámetros:
        ------------
            nombre:str
                    Variable que almacena el nombre de la persona.
        '''
        self.nombre = nombre

    def _repr_(self):
        '''
        Método que administra la propiedad de la persona.
        Retorna el nombre de la persona.
        _repr_(self):Función que administra la propiedad de la persona.
        Return: Nombre de la persona.
        '''
        return f'Persona(nombre={self.nombre})'

    @classmethod
    def save(cls, persona):
        '''
        Método para guardad a la persona en la base de datos.
        
        -----------
        Parámetros:
        -----------
            persona: Variable que almacena a la persona, la cual    
                     va a ser almacenada en la base de datos.
        '''
        print(f'Guardar la {persona} en la base de datos')


if __name__ == '__main__':
    '''
    Función principal llamamos a todas los métodos para 
    cumplir con lo que se necesita.
    '''
    '''
    Instancia de la variable de tipo Person.
    '''
    ciudadano=Person('Mateo Beltran')
    '''
    Se llama al método para guardad a la persona en la base de datos.
    '''
    Person.save(ciudadano)
    