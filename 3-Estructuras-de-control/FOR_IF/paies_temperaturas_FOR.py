"""Devulve la media de temperatura de 4 paises ingresados"""

class Clr(): #Para darle algo de color a la consola
    Red,Green,Yellow,Blue,Magenta,Cyan,End = "\033[31m","\033[32m","\033[33m","\033[34m","\033[35m","\033[36m","\033[0m"


lpaises=[]
ltemperaturas=[]

#Ingreso de datos
print("\nIngrese 4 paises y sus 3 temperaturas medias mensuales\n")
for i in range(3):
   lpaises.append(input(f"\nIngrese Pais {i+1}: "))
   ltemperaturas.append([float(input(f'Ingrese temperatura {t+1} en Cel: ') for t in range(3))])

#Lista de medias
media=[round(sum(m)/3,2) for m in ltemperaturas ]

#Media Mayor
mayor=["",0.0]
for l in range(3):
    if media[l]>mayor[1]:
        mayor[1]=media[l]
        mayor[0]=lpaises[l]

#imprime resultados
for p in range(3):
    print(f'\nPais: {Clr.Green}{lpaises[p]}{Clr.End} Temperaturas: {ltemperaturas[p]}')
    print(f'Media de temperaturas: {media[p]} ')
print(f'\nPais con media mayor: {Clr.Yellow}{mayor}{Clr.End}')





             
           
              
          
    
