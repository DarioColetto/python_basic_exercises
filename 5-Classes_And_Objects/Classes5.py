class Cuadrado:
    """Devuelve perimetro y superficie de un cuadrado""" 
    def __init__(self, lado:float|int):
        self.lado=lado

    def imprimir(self):
        per=self.lado*4
        sup=self.lado*self.lado
        print(f"Perimetro:{per} Superficie:{sup}")


c1=Cuadrado(3).imprimir()
c2=Cuadrado(1.5).imprimir()
        