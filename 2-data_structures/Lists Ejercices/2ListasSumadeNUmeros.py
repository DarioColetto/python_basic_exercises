#Devuelve la suma de los numeros de 2 listas dentro de un array en una nueva lista.



listas=[[1,2,3,4],[2,3,4,5]]
suma=[]


for i in range(len(listas[0])):
    suma.append(listas[0][i]+listas[1][i])
    
     
print(suma)
    
        