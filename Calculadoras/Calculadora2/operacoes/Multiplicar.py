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
        """
        Docstring for __init__
        
        :param self: Description
        :param x: inicia o atributo self.x da instancia da classe multiplicacao com o valor de x
        :param y: inicia o atributo self.y da instancia da classe multiplicacao com o valor de y
        self.resultado  é inicializado  a 0
        """
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