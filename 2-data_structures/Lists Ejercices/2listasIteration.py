#Se pueden escribir las variables en lineas diferentes,

frutas=['banana', 'peras', 'manzanas']
precios=[3.15, 2.18, 1.5  ]

for i in range(len(frutas)):
    print(frutas[i], precios[i])

#Se pueden escribir en una sola linea.

paises,capitales=["Argentina", "Peru", "Espana"],["Buenos Aires", 'Lima', 'Madrid']
print(paises, capitales)

for i in range(len(paises)):
    print(paises[i], capitales[i])