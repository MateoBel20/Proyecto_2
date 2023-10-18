class Cliente:
    '''
    Se creo una clase la cual administra los 
    datos de un cliente.

    ------------
    Métodos:
    ------------
        __init__(self,nombre,apellido,cedula): Construye los datos del cliente.

    -----------
    Atributos:
    -----------
        nombre: Variable que almacena el nombre del cliente.
        apellido: Variable que almacena el apellido del cliente.
        cedula: Variabale que almacena la cédula del cliente.
    '''
    def __init__(self,nombre,apellido,cedula):
        '''
        Construye los datos del cliente.

        -------------
        Parámetros:
        -------------
            nombre: Variable que almacena el nombre del cliente.
            apellido: Variable que almacena el apellido del cliente.
            cedula: Variabale que almacena la cédula del cliente.
        '''
        self.nombre=nombre
        self.apellido=apellido
        self.cedula=cedula

class Bancos:
    '''
    Clase que administra los datos de un banco, 
    le da al cliente el pago que deberá hacer mensualmente.

    ---------
    Métodos:
    ---------
        __init__(self,nombre,interes,meses,capital): Construye los atributos de la clase.
        Calcular(self): Método que se encarga de darle al usuario el dinero que tiene que pagar mensualmente.

    ----------
    Atributos:
    ----------
        nombre: Variable que almacena el nombre del banco
        interes: Variable que almacena el interes propuesto por el banco.
        meses: Variable que almacena el tiempo de pago puesto por el cliente.
        capital: Variable que almacena el monto de capital a pagar.
    
    '''
    def __init__(self,nombre,interes,meses,capital):
        '''
        Método que construye los atributos.

        -----------
        Parámetros:
        -----------
            nombre: Variable que almacena el nombre del banco
            interes: Variable que almacena el interes propuesto por el banco.
            meses: Variable que almacena el tiempo de pago puesto por el cliente.
            capital: Variable que almacena el monto de capital a pagar.
        '''
        self.nombre=nombre
        self.interes=interes
        self.meses=meses
        self.capital=capital
    def Calcular(self):
        '''
        Método que se encarga de darle al 
        usuario el dinero que tiene que pagar mensualmente.

        RETORNA: Valor a pagar.
        '''
        return (self.interes*self.capital)/self.meses

if __name__ == '__main__':
    '''
    Se le pide los datos al usuario para poder
    instanciar de manera dinámica la clase "Cliente".
    '''
    nombreCliente=input("Ingrese su nombre: ")
    apellidoCliente=input("Ingrese su apellido: ")
    cedulaCliente=input("Ingrese su número de cédula: ")
    '''
    Se instancia la clase "Cliente" de manera
    dinámica, se lo hace con lo solicitado anteriormente.
    '''
    persona=Cliente(nombreCliente,apellidoCliente,cedulaCliente)

    '''
    Se le pide los datos al usuario para poder
    instanciar de manera dinámica la clase Bancos.
    '''
    nombreBanco=input("Ingrese el nombre del banco: ")
    interesBanco= float(input("Ingrese el interés del banco: "))
    mesesAPagar=float(input("Ingrese la cantidad de meses: "))
    '''
    Se hace una respectiva estructura de control "while" para 
    decirle al cliente que la deuda no puede superar
    los 24 meses y obviamente no existe meses negativos.
    '''
    while mesesAPagar>24 or mesesAPagar<=0:
        print("No puede ser más de 24 meses la deuda, ingrese nuevamente por favor: ")
        mesesAPagar=float(input("Ingrese la cantidad de meses: "))

    '''
    La variable para pedirle al usuario, con esta variable se 
    podrá crear el total a pagar mensualmente.
    '''
    capitalAPedir=float(input("Ingrese el capital a pedir: "))

    '''
    Se instancia el objeto de tipo "Bancos", esto se hace de 
    manera dinámica con los datos pedidos anteriormente.
    '''
    bancoPreferido=Bancos(nombreBanco,interesBanco,mesesAPagar,capitalAPedir)
    '''
    Se imprime un mensaje que muestra cuanto debe pagar 
    mensualmente el cliente. Se llama al método 
    "Calcular".
    '''
    print("Señor/a", nombreCliente, " ", apellidoCliente, " usted debe cancelar mensualmente $", bancoPreferido.Calcular())
