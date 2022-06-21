def ingreso():
    lista=[]
    for i in range(5):
        lista.append(int(input(f"Ingrese valor {i+1}: ")))
    return lista    

def maxymin(arg):
    maxn=max(arg)
    minn=min(arg) 
    print(f"Numero mayor de la lista: ", maxn)
    print(f"Numero menor de la lista: ", minn)

listanum=ingreso()
maxymin(listanum)
