import pymongo
'''
Se importa la librería "pymongo", la cual va a permitir 
tener los comandos del terminal de mongoDB en el Python.
'''
'''
Se creó una variable "cliente" de tipo "pymongo.MongoCliente".
La cual accede a nuestro mongodb local con su respectiva canal
de llamada.
'''
cliente=pymongo.MongoClient("mongodb://localhost:27017/")
'''
Se crea una base de datos para almacenar las siguientes colecciones.
'''
db=cliente["mibasededatos"]
'''
Se crea una nueva colección denominada "clientes".
'''
col=db["clientes"]

'''
Se insertan datos a la base de datos.
'''

lista=[
    {"nombre": "Mateo", "Apellido": "Lopez","cedula":"1234567890"},
    {"nombre": "Josue", "Apellido": "Hernandez","cedula":"0987654321"},
    {"nombre": "Sebastian", "Apellido": "Gomez","cedula":"091234321"},
]
'''
Se crea una variable, que tenga la función de insertar los elementos 
de las lista previamente ingresados a nuestra colección.
'''
listaDatos=col.insert_many(lista)
