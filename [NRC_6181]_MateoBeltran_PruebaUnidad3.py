'''
Se importa la clase abstracta ABC, la cual obliga 
a las subclases a implementar todos los métodos 
abstractos que se necesiten.
'''
from abc import ABC, abstractmethod
'''
Se importa la librería Mongo para utilizar las propiedad 
de mongo DB en python
'''
import pymongo
class Producto(ABC):
    '''
    Clase abstracta "Producto"

    --------
    Métodos:
    --------
        __init__(self, nombre, precio, cantidad, tipo): Construye los atributos de la clase.
        def coneccionMongo(self): Método que conecta con la base de datos.
        def coneccionMongoAppend(self): Método que agrega datao a la base de datos.
        compra(self, dato, cliente, cantidad): Método que permite comprar al usario.
        verCompras(self,nombreCliente, dato): Método que permite ver la compra del usuario.
    ----------
    Atributos:
    ----------
        nombre: Variable que almacena el nombre del producto.
        precio: Variable que almacena el precio del producto.
        cantidad: Variable que almacena la cantidad del producto.
        tipo: Variable que almacena el tipo de producto que quiere.
    '''
    @abstractmethod
    def __init__(self):
        '''
        Método que construye los atributos de la clase.

        ------------
        Parámetros:
        ------------
            nombre: Variable que almacena el nombre del producto.
            precio: Variable que almacena el precio del producto.
            cantidad: Variable que almacena la cantidad del producto.
            tipo: Variable que almacena el tipo de producto que quiere.
        '''
        self.nombe = None
        self.precio = None
        self.cantidad = None
        self.tipo = tipo
        self.mycol = None
        self.cliente = None
    
    def pasaDatos(self, nombre, cantidad):
        '''
        Método que pasa los datos.
        '''
        self.nombe = nombre
        self.cantidad = cantidad
       

    def coneccionMongo(self):
        '''
        Método que conecta con la base de datos.

        Retorna la colección de la base de datos.
        '''
        micliente=pymongo.MongoClient("mongodb://localhost:27017/")
        mydb=micliente["Arambulo_Beltran_DB"]
        mycol=mydb["COL_Productos"]
        return mycol
    def coneccionMongoAppend(self):
        '''
        Método que agrega datao a la base de datos.

        Retorna la colección de la base de datos.
        '''
        micliente=pymongo.MongoClient("mongodb://localhost:27017/")
        mydb=micliente["Arambulo_Beltran_DB"]
        mycol=mydb["COL_Compras"]
        return mycol


    @abstractmethod
    def compra(self, cliente ):
        '''
        Método que permite comprar al usuario.

        ------------
        Parámetros:
        ------------
            dato: Variable que almacena el dato requerido 
                  por el cliente.
            cliente: Variable que almacena datos del cliente.
            cantidad: Variable que almacena la cantidad de productos.
        '''
        self.cliente = cliente
        coleccion = self.coneccionMongo()
        self.datoEncontrado = coleccion.find_one({'nombre': self.nombe}) 
        precio = self.datoEncontrado['precio']
        nombre = self.datoEncontrado['nombre']

        listaProducto = [{'IDcliente': cliente, 'producto': nombre, 'cantidad': self.cantidad, 'precioPorUnidad': precio}]

        coleccion2 = self.coneccionMongoAppend()
        coleccion2.insert_many(listaProducto)

        
    @abstractmethod
    def verCompras(self, dato):
        '''
        Método que permite ver las compras

        -----------
        Parámetros:
        -----------

            nombreCliente: Variable que almacena el nombre del cliente.
            dato: Variable que almacena el dato del producto que desea el cliente.
        '''
        coleccion = self.coneccionMongoAppend()
        self.datoEncontrado = coleccion.find_one({'IDcliente': self.cliente})
        if dato == 'precio': 
            return self.datoEncontrado['precioPorUnidad']
        if dato == 'producto':
            return self.datoEncontrado['producto']
        if dato == 'cantidad':
            return self.datoEncontrado['cantidad']

class entretenimiento(Producto):
    '''
    Clase hija de la clase "Producto".

    --------
    Métodos:
    --------
        __init__(self,*args, **kwargs ) :Construye los atributos de la clase.
        compra(self, dato, cliente, cantidad): Método que permite comprar.
        verCompras(self, nombreCliente, dato): Método que permite ver las compras. 

    ----------
    Atributos:
    ----------
        Hereda los atributos de la clase padre.
    '''
    def __init__(self,*args, **kwargs ) :
        '''
        Método que construye los atributos de la clase 
        hija.
        '''
        super().__init__(*args, **kwargs)
    
    def compra(self, dato):
        '''
        Método que permite comprar.

        -----------
        Parámetros:
        -----------
            nombre: Variable que almacena el nombre del producto.
            precio: Variable que almacena el precio del producto.
            cantidad: Variable que almacena la cantidad del producto.
        '''
        return super().compra(dato)
    
    def verCompras(self,  dato):
        '''
        Método que permite ver las compras

        -----------
        Parámetros:
        -----------

            nombreCliente: Variable que almacena el nombre del cliente.
            dato: Variable que almacena el dato del producto que desea el cliente.

        Retorna los datos.
        '''
        return super().verCompras( dato)
    
    
        
class hogar(Producto):
    '''
    Clase hija de la clase "Producto".

    --------
    Métodos:
    --------
        __init__(self,*args, **kwargs ) :Construye los atributos de la clase.

    ----------
    Atributos:
    ----------
        Hereda los atributos de la clase padre.
    '''
    def __init__(self,*args, **kwargs ) :
        '''
        Método que construye los atributos de la clase 
        hija.
        '''
        super().__init__(*args, **kwargs)
    
    def compra(self, dato):
        '''
        Método que permite comprar.

        -----------
        Parámetros:
        -----------
            nombre: Variable que almacena el nombre del producto.
            precio: Variable que almacena el precio del producto.
            cantidad: Variable que almacena la cantidad del producto.
        '''
        return super().compra(dato)
    
    def verCompras(self,  dato):
        '''
        Método que permite ver las compras

        -----------
        Parámetros:
        -----------

            nombreCliente: Variable que almacena el nombre del cliente.
            dato: Variable que almacena el dato del producto que desea el cliente.

        Retorna los datos.
        '''
        return super().verCompras( dato)
    
class tangible(Producto):
    '''
    Clase hija de la clase "Producto".

    --------
    Métodos:
    --------
        __init__(self,*args, **kwargs ) :Construye los atributos de la clase.

    ----------
    Atributos:
    ----------
        Hereda los atributos de la clase padre.
    '''
    def __init__(self,*args, **kwargs ) :
        '''
        Método que construye los atributos de la clase 
        hija.
        '''
        super().__init__(*args, **kwargs)
    

    def compra(self, dato):
        '''
        Método que permite comprar.

        -----------
        Parámetros:
        -----------
            nombre: Variable que almacena el nombre del producto.
            precio: Variable que almacena el precio del producto.
            cantidad: Variable que almacena la cantidad del producto.
        '''
        return super().compra(dato)
    
    def verCompras(self,  dato):
        '''
        Método que permite ver las compras

        -----------
        Parámetros:
        -----------

            nombreCliente: Variable que almacena el nombre del cliente.
            dato: Variable que almacena el dato del producto que desea el cliente.

        Retorna los datos.
        '''
        return super().verCompras( dato)
    






if __name__=='__main__':
    '''
    Se llama a la base de datos con sus
    respectivas colección y por ende 
    por los datos 
    '''
    micliente=pymongo.MongoClient("mongodb://localhost:27017/")
    mydb=micliente["Arambulo_Beltran_DB"]
    mycol=mydb["COL_Productos"]
    cliente = input('ingrese su nombre: ')
    '''
    Se crea el menú que le da las opciones 
    al usuario final.
    '''
    while True:
        print('''
        TIENDA DE PRODUCTOS VARIADOS.
        
        1. ORDENAR PRODUCTO.
        2. VER COMPRA.
        3. SALIR''')
        opcion = int(input('Ingrese opcion: '))

        if opcion == 1: 
            '''
            Opcion que permite comprar
            '''
            print('comprar producto')
            datos = mycol.find({}, {'_id':0, 'nombre': 1, 'precio': 1, 'tipo': 1})
            for  dato in datos:
                print(dato)
            tipo = input('ingrese tipo:')
            datos2 = mycol.find({'tipo': tipo},{'_id':0, 'tipo': 1})
            
            if dato['tipo'] == 'entretenimiento':
                ingrese = input('ingrese producto: ')
                ingreseCantidad = input('ingrese cantidad: ')
                entretenimientos = entretenimiento()
                print('entretenimiento')
                entretenimientos.pasaDatos(ingrese, ingreseCantidad)
                entretenimientos.compra(cliente)
            elif dato['tipo'] == 'hogar':
                ingrese = input('ingrese producto: ')
                ingreseCantidad = input('ingrese cantidad: ')
                hogares = hogar()
                hogares.pasaDatos(ingrese, ingreseCantidad)
                hogares.compra(cliente)
                print('hogar')
            elif dato['tipo'] == 'tangible':
                ingrese = input('ingrese producto: ')
                ingreseCantidad = input('ingrese cantidad: ')
                tangibles = tangible()
                print('tangible')
                tangibles.pasaDatos(ingrese, ingreseCantidad)
                tangibles.compra(cliente)

            
        elif opcion == 2:
            print('ver compra')
            if dato['tipo'] == 'entretenimiento':
                    lista = [entretenimientos.verCompras('precioPorUnidad'),entretenimientos.verCompras('producto'), entretenimientos.verCompras('cantidad') ]
                    print(lista)
            elif dato['tipo'] == 'hogar':
                    lista = [hogares.verCompras('precioPorUnidad'),hogares.verCompras('producto'), hogares.verCompras('cantidad') ]
                    print(lista)
            elif dato['tipo'] == 'tangible':
                    lista = [tangibles.verCompras('precioPorUnidad'),tangibles.verCompras('producto'), tangibles.verCompras('cantidad') ]
                    print(lista)

           
        elif opcion == 3:
            print('saliendo')
            break
        else:
            print('error de opcion')
