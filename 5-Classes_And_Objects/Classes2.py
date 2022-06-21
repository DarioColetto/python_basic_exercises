class Alumno:

    def inicializar(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota

    def imprimir(self):
        print("Nombre: ", self.nombre)
        print("Nota: ", self.nota)

    def mostrar_estado(self):
        if self.nota>=5:
            print(self.nombre," aprobado")
        else:
            print(self.nombre," suspendido")    



#princpal

alumno1=Alumno()
alumno1.inicializar("Juan", 2)
alumno1.imprimir()
alumno1.mostrar_estado()

alumno2=Alumno()
alumno2.inicializar("Ana", 6)
alumno2.imprimir()
alumno2.mostrar_estado()

alumno3=Alumno()
alumno3.inicializar("Raquel", 10)
alumno3.imprimir()
alumno3.mostrar_estado()