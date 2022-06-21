
#Listas
listaEmpleados=[]
listaSueldos=[]
#Agrega nombre de empleado y sueldos
num=int(input("Ingrese cantidad de empleados a registrar: "))
for i in range(num): 
    listaEmpleados.append(input(f"Ingrese Nombre de empleado {i+1}: "))                                    
    listaSueldos.append([(int(input(f"Ingrese sueldo {x+1} de {listaEmpleados[i]}: "))) for x in range(3) ])  

#Suma de sueldos de cada empleado     
ingresoAcumulados=[sum(s)for s in listaSueldos]    

#Compara y guarda el valor mas alto
Max=["", 0]
if ingresoAcumulados[i]>Max[1]: 
    Max[1]=ingresoAcumulados[i]
    Max[0]=listaEmpleados[i]

#Imprime resultados:
for p in range(len(listaEmpleados)):
    print(f'Nombre: {listaEmpleados[p]}')    
    print(f'Sueldos: {listaSueldos[p]}')
    print(f'Total acumulados: {ingresoAcumulados[p]}\n')
print('Sueldo maximo Acumulado: ', Max)






