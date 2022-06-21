class Abuelo:
    def __init__(self, apellido:str):
        self.apellido=apellido

class Padre(Abuelo): #Creamos la clase Padre
    ojos = "azules"
    cejas = "Marrones"
    
    def __init__(self ): 
        super().apellido

class Madre: #Creamos la clase Padre
    brazos = "grandes"
    piernas = "cortas"
    def __init__(self ): pass
        
class Hijo(Padre, Madre): #Creamos clase hija que hereda de Padre y luego de Madre
    cara = "linda"
    
    def __init__(self ): pass
        


Pepe=Padre("Lopez")
print(Pepe.apellido)