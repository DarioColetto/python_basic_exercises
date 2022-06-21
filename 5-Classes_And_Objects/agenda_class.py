class Agenda:

    contactos=[]

    def agregar(self, nombre:str, tel:int, mail:str):
        self.contactos.append([nombre,tel, mail] )
        
    def mostrarcontactos(self):
        print("Lista de contactos: ")
        for contacto in self.contactos:
            print(contacto, end="\n")
    
    def buscar(self, nombrebuscado:str):
        long=len(self.contactos)
        aux=0
        for i in range(long) :
            if self.contactos[i][0]==nombrebuscado:
                aux+=1
                print(self.contactos[i])
        if aux==0:
            print(f"El contacto {nombrebuscado} no se encuentra.")        
   


agenda1=Agenda()
agenda1.agregar("Juan", 677552233, 'juan@gmail.com')
agenda1.agregar("Pedro", 674552233, 'pedro@gmail.com')
agenda1.agregar("Pepa", 674778899, 'pepa@gmail.com')

agenda1.buscar('Pedro')