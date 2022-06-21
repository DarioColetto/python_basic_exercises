frase="Pablito clavo un clavito, que clavito clavo Pablito"

#x=(input("Ingrese texto: "))


contador=0
        
for i in frase:  
    if i == ' ':   
         contador+=1

print("Su frase tiene: ", contador, " espacios en blanco.")         