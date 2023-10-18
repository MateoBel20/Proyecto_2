'''
Se importa la librería "pymongo", para poder 
utilizar los comandos de mongo en python
'''
import pymongo
class DbConnectionMeta(type):
    '''
    Clase que se encarga de concetar nuestra colección de nuestra
    base de datos.

    ---------
    Métodos:
    ---------
        __instancecheck__(self, instance):Método que instancia la clase.
        __subclasscheck__(self, subclass):Si la subclase "connect" se llama a las respectivas subclases.

    
    ----------
    Atributos:
    ----------
        instance: Variable que almacena la instancia de la variable.
        subclass: Variable que almacena las diferentes instancias .
    '''
    def __instancecheck__(self, instance):
        '''
        Método que instancia la clase.

        -----------
        Parámetros:
        -----------
            instance: Variable que almacena la instancia de la variable.

        RETORNA: LA INSTANCIA DE LA SUBCLASE
        '''
        return self.__subclasscheck__(type(instance))

    def __subclasscheck__(self, subclass):
        '''
        Si la subclase "connect" se llama a las respectivas subclases.

        -----------
        Parámetros:
        -----------
            subclass: Variable que almacena las diferentes instancias .

        RETORNA: LLAMA A LA SUBCLASE

        '''
        return (hasattr(subclass, 'connect') and callable(subclass.connect))

class DbConnectionInterface(metaclass=DbConnectionMeta):
    '''
    Clase hija vacía de "metaclass=DbConnectionMeta"
    '''
    pass


class MySqlConnection(DbConnectionInterface):
    '''
    Clase que se conecta con los métodos respectivos 
    del programa de Python 

    ---------
    Métodos:
    ---------
        connect: Método que se encarga de conectar.
    '''
    def connect(self):
        '''
        Método que se encarga de conectar, es vacío.
        '''
        pass

class PageLoader():
    '''
    Clase que se encarga de la conexión entra la colección 
    y la interfaz
    
    ----------
    Métodos:
    ----------
        __init__(self, db_connection: DbConnectionInterface): Construye la conexión entre
                                                              la interfaz y la colección del mongoDB.

        verificar(self): Método que verifica si nos conectamos con la base de datos.

    ----------
    Atributos:
    ----------
        db_connection: DbConnectionInterface: Variable que almacena la información de la conexión.
    '''
    def __init__(self, db_connection: DbConnectionInterface):
        '''
        Construye la conexión entre la interfaz y la colección del mongoDB.

        ------------
        Parámetros:
        ------------
           db_connection: DbConnectionInterface: Variable que almacena la información de la conexión. 
        '''
        self._db_connection = db_connection

    def verificar(self):
        '''
        Método que verifica si nos conectamos con la base de datos.
        '''
        midb=self._db_connection["miscelanea"]
        print(midb.list_collection_names())

if __name__=="__main__":
    '''
    Se llama a la colección previamente realizada 
    en talleres anteriores.
    '''
    micliente=pymongo.MongoClient("mongodb://localhost:27017/")
    '''
    Instancia del objeto de tipo "PageLoader"
    '''
    paginaDB=PageLoader(micliente)
    '''
    Se imprime la verificación.
    '''
    print(paginaDB.verificar())
