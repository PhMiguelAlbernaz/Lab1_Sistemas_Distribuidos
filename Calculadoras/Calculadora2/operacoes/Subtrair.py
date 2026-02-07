"""
Docstring for Calculadoras.Calculadora2.operacoes.Subtrair
Classe Diferenca

"""
class Diferenca:
    """
    Docstring for Diferenca
    A funcao diferenca tem o proposito de subtrair os numeros que a mesma recebe nos parametros
    """    
    def __init__(self,x:int,y:int):
        """
        Docstring for __init__
        
        :param self: Description
        :param x: inicia o atributo self.x da instancia da classe Diferenca com o valor de x
        :param y: inicia o atributo self.y da instancia da classe diferenca com o valor de y
        self.resultado  é inicializado  a 0
        """
        self.x = x
        self.y=y
        self.resultado=0

    def diferenca(self):
        """
        Docstring for diferenca
        
        self.resultado toma o valor de   self.x-self.y
        da retorno de self.resultado 
        """

        self.resultado=self.x-self.y
        return self.resultado 