from termcolor import colored

A1=float(input('Ingrese Nota 1: '))
A2=float(input('Ingrese Nota 2: '))
A3=float(input('Ingrese Nota 3: '))

promedio = round((A1+A2+A3)/3)
print(colored("Tu promedio es: " + str(promedio),'magenta'))

if promedio >= 7:
    print(colored('Promociona', 'green'))
else:
    print (colored('Anda a estudiar!', 'red'))    