
print('A continuacion ingresa 10 Notas.')
contador=1
notasAprobadas=0
notasDesaprobadas=0

while contador <= 10:
    try:       
        nota=(float(input("Agrega Nota " + str(contador) + ": ")))
        if nota>=7:
            notasAprobadas+=1
        else:    
            notasDesaprobadas += 1
        contador+=1    
    
    except ValueError:
        print("Eso no es un valor numerico wey!.\nVolvelo a intentar.")


print ('Cantidad de Aprobados: ', notasAprobadas)
print ('Cantidad de Desaprobados: ', notasDesaprobadas)