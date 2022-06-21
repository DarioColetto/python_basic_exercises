#Devuelve la suma de los numeros entre 2 listas en ua nueva lista

#Listas vacias
ln1=[]
ln2=[]
ln3=[]

###Ingreso de datos###
#Lista 1:
print("\nIngrese 4 numeros a lista 1.\n")
for n in range(4):
    ln1.append(int(input("Ingrese numero en lista 1: ")))

#Lista 2:
print("\nIngrese 4 numeros a lista 2.\n")
for n in range(4):
    ln2.append(int(input("Ingrese numero en lista 2: ")))    
    
#Bucle de suma.
for ix in range(4):
    ln3.append(n+ln2[ix])
#Resultado
print("El resultado de la suma es: " , ln3)

