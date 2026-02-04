import math as m
def raizquadrada( x: float) -> float:
    if(x<0):
        raise Exception(" nao podes por  numeros  menores que zero")
    return m.sqrt(x)
