""" De una lista de numeros random, devuelve los multiplos de 3 y 5"""
import random

#-------------------------------#
#Lista de numeros random.
listanum=random.sample(range(0,101),10)
print(listanum)

#Contadores
m3=0
m5=0
m35=0

#Listas
list3=[]
list5=[]
list35=[]

#Bucle 
for i in listanum:
    if i%3== 0 and i%5==0:
        m35+=1
        #Agrega a la lista corespondiente
        list35.append(i)
          
    else:    
        if i%3 == 0:
            m3+=1
            list3.append(i)
            
        elif i%5 == 0:
            m5+=1
            list5.append(i)
        else:
            pass    
                
#Imprime contadores y las listas.
print("Cantidad de multiplos de 3 y 5: ", m35)
print(list35)
print("Cantidad de multiplos de solo de 3: ", m3)
print(list3)
print("Cantidad de multiplos de solo de 5: ", m5)
print(list5)
