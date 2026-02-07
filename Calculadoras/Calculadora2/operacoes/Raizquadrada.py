
import math as m
class RaizQuadrada:
    """
Docstring for RaizQuadrada
a funcao raiz quadrada  que ta dentro da classe RaizQuadrada  tem  como objetivo 
fazer a raiz quadrada da o parametro que a mesma recebe 

    """
    def __init__(self,x):
        """
        Docstring for __init__
        
        :param self: Description
        :param x: inicia o atributo self.x da instancia da classe raizquadrada com o valor de x
        self.resultado  é inicializado  a 0
        """
        self.x=x
        self.resultado=0

    def raizquadrada(self):
        """
        Docstring for raizquadrada
        
        :param x:altera o parametro do  self.x 
        muda  o valor de resultado self.resultado para m.sqrt(self.x)
        da retorno de self.resultado
        """
        
        self.resultado=m.sqrt(self.x)
        return self.resultado

