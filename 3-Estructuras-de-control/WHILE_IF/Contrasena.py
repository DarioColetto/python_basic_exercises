passw=(input("Elija contraseña entre 10 y 20 caracteres: "))

while True:
    passw_len=len(passw)
    
    if passw_len<10 or passw_len>20:

        print("La contraseña introducida no es correcta")

        passw=(input("Elija contraseña entre 10 y 20 caracteres: "))
    else:
        print("Su password ha sido guardado correctamente")
        break    