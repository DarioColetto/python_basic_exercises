"""Simple To Do list hecha con funciones"""

def cargarDatos():
    agenda={}
    continua='s'
    while continua =="s":
        dia=input("Ingrese dia (d/m/aaaa): ")
        listaActividades=[]
        while continua =="s":
            hora=input('Ingrese Hora (hh:mm): ')
            actividad=input("Ingrese actividad: ")
            listaActividades.append((hora, actividad))
            continua=input("Agregar otra actividad? s/n: ")
        continua=input("Agregar otro dia? s/n: ")
        agenda[dia]=listaActividades
    return agenda

def listadoCompleto(age:dict):
    print(age)

def consulta(age:dict):
    diaconsult=input("Ingrese fecha a consultar (d/m/aaaa): ")
    print(age[diaconsult])

#------#    
agenda1=cargarDatos()
listadoCompleto(agenda1)
consulta(agenda1)
