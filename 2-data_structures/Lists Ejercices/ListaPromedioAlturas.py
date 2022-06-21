
print("A continuacion agregue 5 alturas")

listaAlturas=[]

for n in range(1,6):
    alturas= listaAlturas.append (float(input(f"Ingrese  altura {n}: ")))
    

promedio= round(sum(listaAlturas)/ len(listaAlturas),2)

alto=0
bajo=0

for i in listaAlturas:
    if i >promedio: alto+=1
    if i <promedio: bajo+=1

print("Alturas ingresadas: ", listaAlturas)
print ("Promedio de las alturas :" ,promedio)
print(f"Cantidad de altos: {alto} Cantidad de bajos: {bajo}")