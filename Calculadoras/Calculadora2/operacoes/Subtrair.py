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