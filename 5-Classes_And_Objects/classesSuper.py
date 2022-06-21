class Operacion:
    def __init__(self):pass

    def ingresarValores(self):    
        self.valor1=int(input("Intorduzca valor 1: "))
        self.valor2=int(input("Intorduzca valor 2: "))

class Suma(Operacion):
    def __init__(self):
        super().ingresarValores()
        print(f"Suma: {self.valor1+self.valor2}")

class Resta(Operacion):
    def __init__(self):
        super().ingresarValores()
        print(f"Resta: {self.valor1-self.valor2}")   

#---#
Suma()
Resta()