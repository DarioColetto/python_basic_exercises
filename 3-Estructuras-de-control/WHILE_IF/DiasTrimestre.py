while True:
    dia=int(input("Ingrese dia -dd-: "))
    if dia <1 or dia > 31:
        print("***El dia ingresado es invalido.*** \n Ingrese de nuevo.")
        continue
    else:
        print(dia)
        break

while True:
    mes=int(input("Ingrese mes -mm-: "))
    if mes <1 or mes > 12:
        print("***El mes ingresado es invalido.*** \n Ingrese de nuevo.")
        continue
    else:
        break

while True:
    ano=int(input("Ingrese ano -aaaa-: "))
    if ano <1900 or ano > 2100:
        print("***El ano ingresado es invalido.*** \n Ingrese de nuevo.")
        continue
    else:
        break    


if mes <= 3:
    print('El dia ', dia, ' esta dentro del primer trimestre.')
elif mes > 3 or dia <= 6:
    print('El dia ', dia, ' esta dentro del segundo trimestre.') 
elif mes > 6 or dia <= 8:
    print('El dia ', dia, ' esta dentro del tercer trimestre.')
else:
    print('El dia ', dia, ' esta dentro del cuarto trimestre.')                 