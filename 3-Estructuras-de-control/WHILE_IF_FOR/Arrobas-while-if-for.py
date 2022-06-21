#Controla si el mail tiene arrobas y cuantas fueron ingresadas.
#ejemplo pepehotmail.com , pepe@hotmail.com, pepe@@hotmail

#Ingresar mail
mail= input("Ingrese su mail: ")

#loop
while True:
    if '@' not in mail:
        print("Su mail debe tener '@'.")
        mail= input("Reingrese su mail: ")
    else:
        #Contador de arrob@s
        contador=0
        
        for i in mail:  
            if i == '@':   
               contador+=1
        
        print ("Su mail tiene " , contador, "'@'.")
    
        break # Rompe el loop!!  