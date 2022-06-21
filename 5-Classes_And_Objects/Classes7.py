class Alumnos:
    def __init__(self):
        self.nombres=[]
        self.notas=[]

    def menu(self):
        opcion=0
        while opcion !=4:
            print("1-Carga de alumnos")
            print("2-Listado de alumnos")        
            print("3-Aprobados")        
            print("4-Finalizar")
            opcion=int(input("Ingrese opcion: "))

            if opcion==1:
                self.cargar()
            elif opcion==2:
                self.listar()
            elif opcion==3:
                self.notas_altas()
            else:
                print("Programa finalizado")    

    def cargar(self):
        for x in range(5):
            nom=input(f"Ingrese nombre {x+1}: ")
            self.nombres.append(nom)        
            nota=int(input(f"Ingrese nota {x+1}: "))
            self.notas.append(nota)        

    def listar(self):
        print("Listado:")
        for x in range(5):
            print(f"{self.nombres[x]}, {self.notas[x]:>5}")
    def notas_altas(self):  
        print("NOtas Altas: ")
        for x in range(5):
            if self.notas[x]>=7:
                print(f"{self.nombres[x]}, {self.notas[x]:<5}")


alumnos=Alumnos().menu()