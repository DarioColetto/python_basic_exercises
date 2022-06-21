

listaEmpleados=[]
listaSueldos=[]
ingresoAcumulados=[]


for i in range(3):
    nombre=input(f"Nombre de empleado {i+1}: ")
    listaEmpleados.append(nombre)   
    
    sueldos=[]

    for x in range(3):         
        sueldos.append(int(input(f"Ingrese sueldo {x+1} de {nombre}: ")))
    
    listaSueldos.append(sueldos)    
    ingresoAcumulados.append(sum(sueldos)) 

print('Lista de epleados: '+ listaEmpleados)
print('Lista de sueldos: '+ listaSueldos)    
print('Ingresos Acumulados: '+ingresoAcumulados)

Max=["",0]
for n in range(3):
     if ingresoAcumulados[n]>Max[1]:
        Max[1]=ingresoAcumulados[n]
        Max[0]=listaEmpleados[n]

print(Max)


