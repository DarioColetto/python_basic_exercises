strings1=input("Ingrese palabra o frase:")
strings2=input("Ingrese otra palabra o frase:")

def contar_string(par1):
    return len(par1)

cont1=contar_string(strings1)
cont2=contar_string(strings2)

print(f"{strings1} tiene {cont2} caracteres.")
print(f"{strings2} tiene {cont2} caracteres.")

if cont1> cont2:
    print(strings1 ," tiene mas caracteres" )     
elif cont2> cont1:
    print(strings2 ," tiene mas caracteres" ) 
else:
    print("tienen mas caracteres", ) 


