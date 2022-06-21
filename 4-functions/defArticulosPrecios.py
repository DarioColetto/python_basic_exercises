#Funciones
def carga_datos():

    nombres=[]
    precios=[]

    for i in range(5):
        nombre= input(f"Ingrese Nombre de articulo {i+1}: ")  
        nombres.append(nombre)
        precios.append(float(input(f"Ingrese precio de {nombre}: ")))
    return [nombres, precios]

def mayor(arg1, arg2):
    aux=0
    nom=''
    for n in range(5):
        if arg2[n]>aux:
            aux=arg2[n]
            nom=arg1[n]

    return print(f"Precio mayor es de {nom}: {aux} ")        

def importe():
    importe=float(input("\nIngrese un importe: "))
    menores=[[nombres[m], precios[m]] for m in range(5) if precios[m]<=importe]
    print("Los articulos con precio menor al importe son: " ,menores)


#Bloque Principal

print("\nIngrese  5 Articulos\n")
#1
nombres, precios=carga_datos()
#2
articulos=[[nombres[n],precios[n]] for n in range(5)]
print("Lista de articulos ", articulos)    
#3
mayor(nombres, precios)
#4
importe()