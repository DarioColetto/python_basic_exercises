"""Devuelve porcentaje de aciertos segun cantidad de preguntas y cantidad de respuestas"""

while True:
    
    nPregutas=int(input("Ingrese cantidad de Preguntas: "))
    nRespuestasCorrectas=int(input("Ingrese cantidad de respuestas Correctas: "))
        
    if nRespuestasCorrectas > nPregutas:
        print("***El numero de respuestas es mayor el numero de preguntas.*** \n Ingrese de nuevo.")
        continue
    else:
        break

porcentajeCorrectas= (nRespuestasCorrectas * 100) /nPregutas  
print('Porcentaje Correcto: ', '% ', porcentajeCorrectas)
if porcentajeCorrectas >= 90:
    print ("Nivel Maximo")
elif  porcentajeCorrectas >= 75:
    print ("Nivel Medio")
elif  porcentajeCorrectas >= 50:
    print ("Nivel Medio")    
else:
    print ("Fuera de Nivel")  