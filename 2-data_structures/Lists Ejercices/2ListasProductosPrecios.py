

#Crea 2 listas: produtos y precios.  
#El usuario ingresa los valores por teclado.
#El programa devuelve una lista de os productos con valores mayores al primer producto ingresado.
#Adicional:Se agregan algunos colores a la salida de la consola. 

#Listas de prueba:
# productos=['Celular', 'Laptot', 'Licuadora', 'Tv', 'Mesa']
# precios=[100.0, 500.54, 50.30, 299.99, 25.15]

#-----#
#Estructura de datos: Listas, Variables
#Conceptos basicos: input(), print(), append(), 
#Conceptos avanzados: zip(), List-comprehension, parsing, import, string-interpolation  

import Colores 

print(f"{Colores.Blue}A continuacion ingrese 5 productos: {Colores.End}")
productos=[]
precios=[]

for i in range(1,6):
    producto=input(f"Ingrese producto {i}: ")
    productos.append(producto)
    precio=float(input(f"Ingrese precio del producto {i}: "))
    precios.append(precio)


datos=zip(productos, precios)

mayoresAprimero=[i for i in datos if i[1]>precios[0] ]

print(f"{Colores.Green}Lista de productos con precio mayor al primero:{Colores.End}", mayoresAprimero)
