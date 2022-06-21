import random


list1= random.sample(range(1, 100), 15)
print('Esta es la Lista 1: ',list1)

list2= random.sample(range(1, 100), 15)
print('Esta es la Lista 2: ',list2)

num1=0
num2=0

for i in list1:
    if num1<i:
        num1=i

for i in list1:
    if num1<i:
        num1=i

if num1>num2:
    print('El numero ', num1, ' de la lista 1, es el mayor.')
elif num1<num2:   
    print('El numero ', num2 , ' de la lista 1, es el mayor.')
else:
    print('Los numeros son iguales')    