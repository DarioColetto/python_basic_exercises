
#Listas
listaEmpleados=[]
listaSueldos=[]
ingresoAcumulados=[]
Max=["",0]

num=int(input("Ingrese Numero de empleados a registrar: "))

for i in range(num): #Agrega nombre de empleado
    nombre=input(f"Nombre de empleado {i+1}: ") 
    listaEmpleados.append(nombre)   
    
    sueldos=[]#Agrega 3 valores/sueldo por cada empleado. 
    for x in range(3):         
        sueldos.append(int(input(f"Ingrese sueldo {x+1} de {nombre}: ")))
    
    #Una vez que aregra los valores:
    listaSueldos.append(sueldos)  #Agrega sueldos a la lista mayor.  
    ingresoAcumulados.append(sum(sueldos)) #agrega la suma de los sueldos

    if ingresoAcumulados[i]>Max[1]: #Compara y guarda el valor mas alto
        Max[1]=ingresoAcumulados[i]
        Max[0]=listaEmpleados[i]

#Imprime resultados:
print('Lista de empleados: ' ,listaEmpleados)
print('Lista de 3 ultimos sueldos: ' , listaSueldos)    
print('Ingresos Acumulados: ',ingresoAcumulados)
print('Sueldo maximo Acumulado: ', Max)






