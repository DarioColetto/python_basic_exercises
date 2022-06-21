class Punto:
    """Averigua el cuadrante"""
    def __init__(self, x:int, y:int):
        self.x, self.y=x, y

    def cuadrante(self):
        if self.x>0 and self.y>0:
            print(f"({self.x},{self.y}) Cuadrante 1")
        elif self.x<=0 and self.y>0:
            print(f"({self.x},{self.y}) Cuadrante 2")
        elif self.x<0 and self.y<0:
            print(f"({self.x},{self.y}) Cuadrante 3")
        elif self.x>0 and self.y<0:
            print(f"({self.x},{self.y}) Cuadrante 4")
        else: 
            print("La coordenada ocupa + de 1 cuadrante.Los valores deben ser mayores a 0.")
         
        

p1=Punto(1,1).cuadrante()
p2=Punto(-1,2).cuadrante()
p3=Punto(0,-1).cuadrante()