#Funciones
def carga_datos():

    nombres=[]
    edades=[]

    for i in range(5):
        nombre= input(f"Ingrese Nombre de persona {i+1}: ")  
        nombres.append(nombre)
        edades.append(int(input(f"Ingrese Edad de persona {nombre}: ")))
    return [nombres, edades]

def mayores18(arg1, arg2):
    mayores=[[arg1[n], arg2[n]] for n in range(len(arg1)) if arg2[n]>=18]
    if len(mayores)>0: 
        return print("Personas mayores son: ", mayores)        

def promedioedades(arg):
    return sum(arg)/5

#Bloque

print("\nIngrese datos de 5 personas\n")
nombres, edades=carga_datos()
mayores18(nombres, edades)
print("El promedio de edad es: ",promedioedades(edades))
