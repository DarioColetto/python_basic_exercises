cantidadEmpleados=int(input("Ingrese la cantidad de empleados: "))

sueldos=[]

for x in range(cantidadEmpleados):
    sueldos.append(int(input("Ingrese sueldo " +str(x+1)+" :")))

#El camino facil...  :P
print(sorted(sueldos))