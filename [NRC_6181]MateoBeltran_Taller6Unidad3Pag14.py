import code
'''
La clase "WorkerMeta, es un ejemplo para ver de una manera 
de un manager"

    ---------
    Métodos:
    ---------
        __instancecheck__(self, instance): Método que instancia la clase.
        __subclasscheck__(self, subclass): Si la subclase "take_break" y la subclase
                                           "get_paid", se llama a las respectivas subclases.

    ----------
    Atributos:
    ----------

        instance: Variable que almacena la instancia de la variable.
        __subclasscheck__(self, subclass): Variable que revisa las subclases.
'''
class WorkerMeta(type):
    '''
    La clase "WorkerMeta, es un ejemplo para ver de una manera 
    de un manager"
    '''
    def __instancecheck__(self, instance):
        '''
        Método que instancia la clase.

        -----------
        Parámetros:
        -----------
            instance: Variable que almacena la instancia de la variable.


        RETORNA LA INSTANCIA
        '''
        return self.__subclasscheck__(type(instance))

    def __subclasscheck__(self, subclass):
        '''
        Si la subclase "take_break" y la subclase
        "get_paid", se llama a las respectivas subclases.
        

        ----------
        Parámetros:
            subclass= Subclase
        '''
        return (hasattr(subclass,'take_break')and callable(subclass.take_break)) \
            and (hasattr(subclass,'get_paid') and callable(subclass.get_paid))


class WorkerInterface(metaclass=WorkerMeta):
    '''
    Clase para saludar
    '''
    def mensaje(self):
        '''
        Método para saludar
        '''
        print('Hola yo trabajo en la empresa')


class ClientFacerMeta(type):
    '''
    Método para el cliente

    -----------
    Métodos:
    -----------
        __instancecheck__(self, instance): Método que instancia la clase.
        __subclasscheck__(self, subclass): Si la subclase "call_client" se llama a las respectivas subclases.

    -----------
    Atributos:
    -----------
        instance: Variable que almacena la instancia de la variable.
        __subclasscheck__(self, subclass): Variable que revisa las subclases.
    '''
    def __instancecheck__(self, instance):
        '''
        Método que instancia la clase.
        '''
        return self.__subclasscheck__(type(instance))

    def __subclasscheck__(self, subclass):
        '''
         Si la subclase "call_client" se llama a las respectivas subclases.
        '''
        return (hasattr(subclass, 'call_client') and callable(subclass.call_client))

class ClientFacerInterface(metaclass=ClientFacerMeta):
    '''
    Método para saludar
    '''
    def mensaje(self):
        '''
        Método para saluda
        '''
        print('Hola necesito un producto')

class CoderMeta(type):
    '''
    Método para el cliente

    -----------
    Métodos:
    -----------
        __instancecheck__(self, instance): Método que instancia la clase.
        __subclasscheck__(self, subclass): Si la subclase "write_code" se llama a las respectivas subclases.

    -----------
    Atributos:
    -----------
        instance: Variable que almacena la instancia de la variable.
        __subclasscheck__(self, subclass): Variable que revisa las subclases.
    '''
    def __instancecheck__(self, instance):
        '''
        Variable que almacena la instancia de la variable.
        '''
        return self.__subclasscheck__(type(instance))

    def __subclasscheck__(self, subclass):
        '''
        Variable que revisa las subclases.
        '''
        return (hasattr(subclass, 'write_code') and callable(subclass.write_code))

class CoderInterface(metaclass=CoderMeta):
    '''
    Clase para saludar
    '''
    def mensaje(self):
        '''
        Método para saludar
        '''
        print('Hola soy Admin')


if __name__=="__main__":
    '''
    Se instancia los objetos de WorkerInterface()
    ClientFacerInterface() y CoderInterface()
    '''
    manager=WorkerInterface()
    developer=ClientFacerInterface()
    coder = CoderInterface()
    '''
    Se imprimen los mensajes
    '''
    print(coder.mensaje())
    print(type(manager.mensaje()))
    print(type(developer.mensaje()))
