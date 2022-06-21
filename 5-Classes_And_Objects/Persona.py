class Persona:
    def __init__(self, nombre:str, edad:int, sexo:str):
        self.nombre=nombre
        self.edad=edad
        self.sexo=sexo

    def datosPersona(self):
        print(f"Mi nombre es {self.nombre}, tengo {self.edad} y soy {self.sexo}")


conrad=Persona("Conrad", 32, "Hombre")
jalapena=Persona("Jalapena", 38, "Mujer")

conrad.datosPersona()
jalapena.datosPersona()

