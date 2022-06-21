"""Ingresa 5 sueldos y los devuelve ordenados en una lista"""

#El _ saltea el nombre de la variable de iteracion. 

sueldos=[int(input(f"Ingrese sueldo {_} : ")) for _ in range(1,6)]  
print(sorted(sueldos))


