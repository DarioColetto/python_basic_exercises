#https://pythones.net/decoradores-en-python-oop/

#


class midecorador(object):
    def __init__(self, func): #Damos como parámetro una función
        print ("""He construido la clase""")
        self.func = func #La almacenamos en el constructor
        
        
    def __call__(self): #La definimos como llamable
        print ("Soy una clase llamada mediante call")
        self.func() #Ejecutamos la funcion en call
        
@midecorador
def hablar():
    print ("Hola soy la función hablar")

hablar() #Llamamos la función decorada