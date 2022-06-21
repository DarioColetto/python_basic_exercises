
pareja=[]
hijos=[]

for i in range(2):
    print(f"Ingrese datos de pareja {i+1}.")
    pareja.append([(input(f"Ingrese nombre {p+1}: ")) for p in range(2)])
    cantidadHijos=int(input(f'Ingrese cantidad de hijos de pareja {i+1}: '))
    hijos.append([(input(f"Ingrese hijo {h+1}: ")) for h in range(cantidadHijos)])

for x in range(len(pareja)):
    print(f'Pareja {x+1}: {pareja[x]} Hijos: {hijos[x]}')