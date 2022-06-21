# Reibir Parametros

#    A                      #B
def funcion_decoradora(funcion_parametro):
    
         #C               
    def funcion_interior(*args, **kwargs):
        # acciones adicionales, se escbibe el codigo adicional.
        print("vamos a realizar un calculo")
        funcion_parametro(*args, **kwargs)

        # Acciones adicionales que decoran

        print("hemos terminado el calculo")
                
                #C
    return funcion_interior


@funcion_decoradora
def suma(num1,num2, num3):
    print(num1+num2+ num3)

@funcion_decoradora
def resta(num1,num2):
    print(num1+num2)

def potencia(base, exponente):
    print(pow(base, exponente))

suma(7, 5, 8)
resta(12,10) 

potencia(base=5, exponente=2)