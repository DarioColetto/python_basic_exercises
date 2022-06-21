listas=[[4,12,5,56],[14,6,25],[3,4,5,67,89,23,1],[78,56]]

for lista in listas:
    for i in range(len(lista)):
        if lista[i]> 10:
            lista[i]=0

print(listas)        