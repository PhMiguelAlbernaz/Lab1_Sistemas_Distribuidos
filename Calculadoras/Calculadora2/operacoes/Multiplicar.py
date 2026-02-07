"""
Docstring for Calculadoras.Calculadora2.operacoes.Multiplicar
classe Multiplicacao 
"""
class Multiplicacao:
    """
    Docstring for multiplicacao
    a funcao  multiplicacao tem como objetivo multiplicar 2 valores 
    """
    def __init__(self,x,y):
        self.x = x
        self.y=y
        self.resultado=0

    def multiplicacao(self):
        """
        Docstring for multiplicacao
        
        :param x: inteiro   
        :param y: inteiro 
        """
        self.resultado=self.x*self.y
        return self.resultado 