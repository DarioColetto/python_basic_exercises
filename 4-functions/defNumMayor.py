def num_mayor(par1, par2):
    if par1> par2:
        return par1
    else:
        return par2    

num1=int(input("Ingrese un valor 1:  "))
num2=int(input("Ingrese un valor 2:  "))

print("El valor mayor es: ", num_mayor(num1, num2))
