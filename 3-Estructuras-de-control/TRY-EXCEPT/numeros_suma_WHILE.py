
numeros=0
sumaNum=0
#id de valores que se van a ingresar en mensaje
idValor=1

#Uso un While para insertar los numeros en la lista con limite 3.
while len(numeros) < 3:    
    try:
        numeros.append(int(input("Escriba el valor " + str(idValor) + " : ")))
        if numeros == numeros:
            sumaNum=+numeros

    except ValueError:
        print("Escribiste mal algo.\nVolvelo a intentar.")

#Uso un loop para recorrer la lista y que me saque 2 mensajes diferentes.
