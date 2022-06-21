class Operaciones:
    """Realiza operaciones matematicas simples."""
    def __init__(self, valor1:int|float, valor2:int|float):
        self.valor1=valor1
        self.valor2=valor2

    def sumar(self):
        print(self.valor1+self.valor2)
    def restar(self):
        print(self.valor1-self.valor2)
    def multiplicar(self):
        print(self.valor1*self.valor2)
    def dividir(self):
        print(self.valor1/self.valor2)


# op1=Operaciones(2,3)
# op1.sumar()
# op1.restar()
# op1.dividir()
# op1.multiplicar()

