"""
Docstring for Calculadoras.Calculadora2.operacoes.Dividir
classe Divisao
"""
class Divisao:
    """
 Docstring for Divisao
 funcao divisao que tem como proposito dividir dois numeros que sao impostos pelos parametros

    """  
    def __init__(self,x,y):
        """
        Docstring for __init__
        
        :param self: Description
        :param x: inicia o atributo self.x da instancia da classe Divisao com o valor de x
        :param y: inicia o atributo self.y da instancia da classe Divisao com o valor de y
        self.resultado  é inicializado  a 0
        """
        self.x = x
        self.y=y
        self.resultado=0

    def divisao(self,x:int,y:int):
        """
        Docstring for divisao
        
        
        :param x: dividendo   
        :param y: divisor
        """
        self.x=x
        self.y=y
        self.resultado=x/y
        return self.resultado # divide o valor de x por y
    


