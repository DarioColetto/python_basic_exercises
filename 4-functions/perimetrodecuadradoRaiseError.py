def perimetrodecuadro(lado:int):
    """Devuelve el preimetro de un cuadrado"""
    if not isinstance(lado, int):
        raise TypeError("Se esperan int como parametros")
    else:
        return lado*4

print(perimetrodecuadro(3.3))
