
numeroPersonas=int(input("Ingrese Numero de personas a introducir: "))

contador=0
suma=0

while contador < numeroPersonas :
    try:
        contador += 1       
        suma+=int(input("Agrega altura en cm. Persona " + str(contador) + ": "))
        
    except ValueError:
        print("Eso no es un valor numerico wey!.\nVolvelo a intentar.")

promedio= suma/contador
print ("Promedio de alturas: ", promedio)