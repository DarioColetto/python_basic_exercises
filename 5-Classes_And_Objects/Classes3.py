class Persona:
    def __init__(self, nombre:str, edad:int):
        self.nombre=nombre
        self.edad=edad

    def mostrarDatos(self):
        print("Nombre :", self.nombre)
        print("Edad: ", self.edad)

        if self.edad>=18:
            print(f"{self.nombre} es mayor de edad.")    


persona1=Persona("Pepe", 34).mostrarDatos()
persona2=Persona("Agustina", 15).mostrarDatos()
persona3=Persona("Josefa", 18).mostrarDatos()