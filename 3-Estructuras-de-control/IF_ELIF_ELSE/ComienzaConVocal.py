"""Verifica si un nombre empieza con vocal"""


vocales=["a","e","i","o","u"]

nombre= input("Ingrese un nombre: ").lower()
    
if nombre[0] in vocales:
    print( nombre, "Comienza con vocal.")        
else:
    print( nombre, "No mienza con vocal.") 

