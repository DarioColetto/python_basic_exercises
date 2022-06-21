
class Clr(): Red,Green,Yellow,Blue,Magenta,Cyan,End = "\033[31m","\033[32m","\033[33m","\033[34m","\033[35m","\033[36m","\033[0m"

lempleados=[]
ldiasFaltados=[]

#Ingreso de datos
print("\nIngrese 3 empleados: \n")
for i in range(3):
    lempleados.append(input(f"\nIngrese Nombre de Empleado {i+1}: "))
  
    dias=[]
    dias= [int(d) for d in input("Ingrese dias: ") if d!="," ]
    ldiasFaltados.append(dias)

#Lista de cantidadInass
cantidadInas=[ len(m) for m in ldiasFaltados ]

#cantidadInas Mayor
mayor=["",0]
for l in range(3):
    if cantidadInas[l]>mayor[1]:
        mayor[1]=cantidadInas[l]
        mayor[0]=lempleados[l]
menores=[]
for l in range(3):
    if cantidadInas[l]<mayor[1]:
        menores.append(f'{lempleados[l]}:{cantidadInas[l]}')      

#imprime resultados
for p in range(3):
    print(f'\nNombre: {Clr.Green}{lempleados[p]}{Clr.End} Dias de Inasistencias: {ldiasFaltados[p]}')
    print(f'Total de Inasistencias: {cantidadInas[p]} ')
print(f'\nEmpleados con menos inasistencias: {Clr.Yellow}{menores}{Clr.End}')