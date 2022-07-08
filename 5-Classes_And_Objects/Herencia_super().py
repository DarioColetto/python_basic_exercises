class Animal(object):
    """Super clase, devuelve un srtring"""
    def __init__(self, animal_type:str) -> str:
        print("Animal Type: ", animal_type)
        

class Mammal(Animal):
    """Hereda de Animal, el metodo super().__init__ realiza las funciones de clase padre"""
    def __init__(self):
        super().__init__("Mammal")
        print("Tiene sangre caliente")


class Dog(Mammal):
    def __init__(self):
        super().__init__()
        print("Tiene 4 patas y dice guau")

sparky=Animal("Es un animal")

pinky=Mammal()

pepi=Dog()        