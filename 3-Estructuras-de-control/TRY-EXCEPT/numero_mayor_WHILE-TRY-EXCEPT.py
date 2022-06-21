

while True:
    try:
        numero = float(input("Humano, ingresa un numero: "))
        numero=len(str(numero).replace('.',''))
        if numero > 2:
            print('Su numero es mayor a 2 digitos.')

        break
    except ValueError:
        print("Oops!  Escribiste cualquiera.  Vamos de nuevo...")



  

