#se establece una funcion A que recibe una por parametro una funcion B y devuelve una funcion C

#    A                      #B
def funcion_decoradora(funcion_parametro):
    
         #C               
    def funcion_interior():
        # acciones adicionales, se escbibe el codigo adicional.
        print("vamos a realizar un calculo")
        funcion_parametro()

        # Acciones adicionales que decoran

        print("hemos terminado el calculo")
                
                #C
    return funcion_interior





@funcion_decoradora
def suma():
    print(15+20)

@funcion_decoradora
def resta():
    print(30-10)

suma()
resta()     