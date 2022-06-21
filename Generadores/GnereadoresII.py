#devuelve las letras de cada ciudad, evitando hacer un bucle anidado

def devuelve_ciudades(*ciudades): # "*" para agregar la cantidad de parametros que quiera.. 
    for ciudad in ciudades:
        yield from ciudad

ciudadesDevueltas= devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "Santander")

print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))