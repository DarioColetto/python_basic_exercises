
#Variables
sueldo=0
Antiguedad=0

#Loop para Ingresar Sueldo.
while True:    
    try:
        sueldo=(float(input("Ingrese Sueldo :"  )))  
        break
    except ValueError:
        print("Escribiste mal algo.\nVolvelo a intentar.")
#Loop para Ingresar Edad.
while True:    
    try:
        antiguedad=(float(input("Escriba el valor de Antiguedad :"  )))
        break        
    except ValueError:
        print("Escribiste mal algo.\nVolvelo a intentar.")        

#Condicion para el salario
if sueldo<500 and antiguedad >= 10:
    sueldo*=1.20
elif sueldo <500 and antiguedad <10:
    sueldo*=1.05
else:    
    pass
#Mensaje
print("Sueldo segun antiguadad es: ", sueldo)