
print("Oiga, Ingrese 10 numeros wey!")

numeros = []
contador=1

while contador <= 10:
    try:       
        numeros.append(int(input("Agrega numero " + str(contador) + ": ")))
        contador += 1
    except ValueError:
        print("Eso no es un valor numerico wey!.\nVolvelo a intentar.")

promedio= sum(numeros)/contador
print ("Promedio: ",promedio)