#Importo el modulo termcolor
from termcolor import colored

#codigo sencillo agregando colorcito al texto
sueldo= int(input("Ingrrese su sueldo: "))
if sueldo > 3000:
    print("Pagar impuestos o a la " + colored("CARCEL !!!", 'red'))
    print("Fin del if")

print(colored("Fin de programa", 'green'))