"""Ingresa nombre y sueldo de empleados. Elimina > a 1000"""

#Inreso de datos
ne=int(input("Cuantos empleados va a ingresar? "))

lempleados=[]
sueldos=[]
for e in range(ne):
    lempleados.append(input(f"Ingrese Nombre de empleado {e+1}: "))
    sueldos.append(int(input(f"Ingrese sueldo de {lempleados[e]}: ")))

#Elimina
i=0
while i < len(sueldos):
    if sueldos[i] >1000:
        lempleados.pop(i)
        sueldos.pop(i)
    else:
        i+=1    
#imprime
print("\nResultados:")
for i in range(len(lempleados)):
    print(F'Nombre: {lempleados[i]} Sueldo: {sueldos[i]} ')        
