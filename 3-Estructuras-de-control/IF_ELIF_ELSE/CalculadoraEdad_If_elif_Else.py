
from datetime import datetime

current_year =  datetime.today().year

#codigo para calcular edad
añoNac=int(input('Dime tu año de nacimiento: '))
tuEdad= current_year- añoNac
print("Tu edad Humana es: " + str(tuEdad))


# Metemos un if por deporte
if tuEdad < 0 :
    print("Aun no naciste o venis del futuro")
elif tuEdad <= 18:
    print ("Sos menor de edad, anda a dormir o viene el coco")
elif tuEdad >= 18 and tuEdad <=80:
    print ("Sos mayor")
else:
    print("Sos vampiro?")    

#otra edad
print("Tu edad en años perro es: " + str(tuEdad*7))


