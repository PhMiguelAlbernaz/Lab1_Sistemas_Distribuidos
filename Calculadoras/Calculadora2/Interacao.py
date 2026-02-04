import operacoes.Dividir as Dividir,operacoes.Subtrair as Subtrair,operacoes.Somar as Somar,operacoes.Multiplicar as Multiplicar,operacoes.Raizquadrada as Raizquadrada 
class Interacao: 
    def excute(self):
        print("Preciso que introduza dois valores:")
    x: float = float(input("x="))
    y: float = float(input("y="))

    # Teste
    # print(res)
    print("soma:",Somar.Soma.somar("",x,y))
    print("diferenca:",Subtrair.Diferenca.diferenca("",x,y))
    try:
        print("divisão:",Dividir.Divisao.divisao("",x,y))
    except: ZeroDivisionError("não  é possivel dividir um numero por 0")
    print("multiplicação:",Multiplicar.multiplicacao.multiplicacao("",x,y))
    print("raiz quadrada  de x:",Raizquadrada.RaizQuadrada.raizquadrada("",x))
print(Interacao.excute)