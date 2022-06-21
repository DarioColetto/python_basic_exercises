def producto_num(lista_n):

    acum_multi=1

    for x in range(len(lista_n)):

        acum_multi*=lista_n[x]

    return acum_multi

   

#pgm principal

lista=[2,4,6,8,10]

print("el producto de todos los números es igual a=> ", producto_num(lista))