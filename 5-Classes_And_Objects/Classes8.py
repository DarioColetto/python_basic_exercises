class Cuenta:
    def __init__(self):
        self.nombre=input("Ingrese titular de cuenta: ")
        self.monto=int(input("Ingrese monto"))
    def verDatos(self):
        print(f"Nombre: {self.nombre} Monto: {self.monto}")    

class CajaAhorro(Cuenta):
    def __init__(self):
        super().__init__()

class PlazoFijo(Cuenta):
    def __init__(self):
        super().__init__()
        print("Total intereses a 30 dias:", self.intereses30dias())

    def intereses30dias(self):
        return self.monto*1.15

#persona1=CajaAhorro().verDatos()
persona2=PlazoFijo()