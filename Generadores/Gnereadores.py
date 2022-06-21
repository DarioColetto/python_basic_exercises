
def generarPares(limite): # Funcion generadora
    num=1

    while num<limite:
        yield num*2
        num+=1   #No olvidarse del incrementador
        
devuelvePares=generarPares(10) #almacena los numeros en una vairable objeto


print(next(devuelvePares)) # Con next() se devuelve el primer valor generado
print("Aqui poridra haber mas codigo....")

print(next(devuelvePares)) #despues el siguiente....
print("Aqui poridra haber mas codigo....")

print(next(devuelvePares))  #despues el siguiente....
print("Aqui poridra haber mas codigo....")