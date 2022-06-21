def decorador(func):
    def nueva_funcion(instancia, parametro1):
        print ("Perro dice:")
        func(instancia, parametro1) 
    return nueva_funcion 

class perro(object):
    def __init__(self, nombre): 
        self.nombre = nombre 
    @decorador 
    def saluda(self, mensaje): 
        self.mensaje = mensaje 
        print(mensaje)
        print("Guau!") 
    @decorador
    def ordeno(self, orden):
        self.orden = orden
        print(orden)
        print("La pata, la pata afgsad! Guau!")

maty = perro('Maty')
maty.saluda('Uso Puppy Linux!')
maty.ordeno('Doy la pata')