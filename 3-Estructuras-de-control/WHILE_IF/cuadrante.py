#Modulo time
import time

#Variables x e y.

x=0
y=0
#Sencillo dialogo del programa
print("A continuacion escriba las coordenadas de navegacion X e Y.")
time.sleep(2)
print("Capisci?")
time.sleep(2)
#Una funcion para imprimir mensaje de error si el valor ingresado es 0.
def errorZero():
    print("El valor no puede ser 0. Intente de nuevo." )

#Loop para Ingresar X.
while True:    
    try:
        x=(int(input("Escriba el valor de x :"  )))
        if x == 0:
            errorZero()
        else:    
            break
    except ValueError:
        print("Escribiste mal algo.\nVolvelo a intentar.")
#Loop para Ingresar Y.
while True:    
    try:
        y=(int(input("Escriba el valor de y :"  )))
        if y == 0:
            errorZero()
        else:    
            break        
    except ValueError:
        print("Escribiste mal algo.\nVolvelo a intentar.")        
print("Las coordenadas son: ","x: ", x,"y : ",y)

#Condicion para el cuadrante.            
if x >0 and y > 0:
    print( "1er cuadrandte.")
elif x < 0 and y > 0:
    print( "2do cuadrandte.")
elif x < 0 and y < 0:
    print( "3er cuadrandte.")
else :
    print( "4to cuadrandte.")            

#Mensaje de final
time.sleep(1)

print("\nGrazie por navegare con noi.")    