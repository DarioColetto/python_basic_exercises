def perimetrodecuadro(lado:int):
    if not isinstance(lado, int):
        raise TypeError("Se esperan int como parametros")
    else:
        return lado*4

print(perimetrodecuadro(3.3))
