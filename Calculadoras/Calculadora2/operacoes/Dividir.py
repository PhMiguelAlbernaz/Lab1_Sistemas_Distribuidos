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
    


