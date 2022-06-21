"""Ingresa nombre y edad. Devuelve lista de mayores de edad"""

# personas=['Raul', 'Cristian', 'Josefa', 'Ursula', 'Maria']
# edades=[12,18, 23, 45, 10]

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
