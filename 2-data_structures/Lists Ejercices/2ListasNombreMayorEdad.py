#Devuelve una lista de personas mayores de edad a partir del ingreso de datos por el usuario.

personas=[]
edades=[]

for i in range(1,6):
    nombre=input(f"Ingrese nombre {i}: ")
    personas.append(nombre)
    edad=int(input(f"Ingrese edad {i}: "))
    personas.append(edad)

datos=zip(personas, edades)

mayoresEdad=[i for i in datos if i[1]>=18 ]
print("Mayores de edad: ", mayoresEdad)
