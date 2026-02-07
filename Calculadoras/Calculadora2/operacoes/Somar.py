"""
classe Soma
"""
class Soma:
    """
    Docstring for Soma
    funcao somar que tem como proposito somar dois numeros
    """
    def __init__(self,x:int,y:int):
        self.x = x
        self.y=y
        self.resultado=0

    def soma(self):
        """
        Docstring for soma
        
        o valor de self.resultado  muda  self.x/self.y 
        da retorno de self.resultado
        """
        self.resultado=self.x+self.y
        return self.resultado 


