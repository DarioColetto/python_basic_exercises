import random

n1=random.randint(0,100)
n2=random.randint(0,100)

list1=0
list2=0
contador=1

while contador<=15:
    if list1 < n1:
        list1=n1
    if list2<n2:
        list2=n2
    contador+=1        

if list1>list2:
    print('El numero ', list1, ' de la lista 1, es el mayor.')
elif list1<list2:   
    print('El numero ', list2 , ' de la lista 1, es el mayor.')
else:
    print('Las listas son iguales')    