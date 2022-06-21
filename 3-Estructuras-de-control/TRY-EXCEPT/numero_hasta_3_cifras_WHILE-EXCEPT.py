
while True:
    try:
        numero = abs(int(input("Humano, ingresa un numero menor a 3 cifras: ")))
        numero=len(str(numero))
        

        if numero == 1:
            print('Su numero tiene 1 digito.')
        elif numero == 2:
            print('Su numero tiene 2 digitos.') 
        elif numero == 3:
            print('Su numero tiene 3 digitos.')
        else:  
            print('El numero no debe ser nulo y debe ser menor a 4 cifras')
        
        break
    except ValueError:
        print("Oops!  Escribiste cualquiera.  Vamos de nuevo...")
             