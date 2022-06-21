#https://pythones.net/decoradores-en-python-oop/

#Ej Decorando una funcion con una clase
#__call__ hace que se llame la funcion automaticamente



class midecorador(object):
    def __init__(self, func): #Damos como parámetro una función
        print ("He construido la clase")
        func() #Llamamos a la función
        
    def __call__(self): #La definimos como llamable
        print ("Soy una clase llamada mediante call")
        
def hablar():
    print ("Hola soy la función hablar")


matias = midecorador(hablar) #instanciamos y llamamos la función hablar brindandola como argumento