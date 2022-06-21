valorBruto= float(input("Ingrese valor de producto:"))
iva=float(input("Ingrese IVA % :"))/100
ivaP=round((valorBruto*iva),2)

print('Valor bruto: ' + str(valorBruto))
print("Iva del producto: " + str(ivaP) + '%')
print('Valor Total: ' + str(valorBruto+ivaP))


