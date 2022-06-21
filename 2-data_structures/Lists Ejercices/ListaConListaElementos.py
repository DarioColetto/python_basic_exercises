#Saca una lista de elementos que incluye listas crecientes.

listaA=[]

for e in range(3):
    listaA.append([])
    for num in range(e+1):
        listaA[e].append(input("ingrese Elemento:"))

print(listaA)


