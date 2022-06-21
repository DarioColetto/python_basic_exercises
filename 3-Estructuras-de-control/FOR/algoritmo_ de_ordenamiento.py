"""Ejemplo de bucle for anidado"""

numeros=[4, 3, 5, 2, 1]
print("lista A: ", numeros)

for k in range(4):

    for x in range(4):
        
        if numeros[x]>numeros[x+1]:
            aux=numeros[x]
            numeros[x]=numeros[x+1]
            numeros[x+1]=aux

print("lista ordenada:", numeros)
    
        