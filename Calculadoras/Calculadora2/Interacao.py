import operacoes.Dividir as Dividir,operacoes.Subtrair as Subtrair,operacoes.Somar as Somar,operacoes.Multiplicar as Multiplicar,operacoes.Raizquadrada as Raizquadrada 
class Interacao: 
    def excute(self):
        print("Preciso que introduza dois valores:")
    x: int = int(input("x="))
    y: int = int(input("y="))

    # Teste
    # print(res)
    print("soma:",Somar.Soma.somar("",x=int,y=int))
    print("diferenca:",Subtrair.Diferenca.diferenca("",x,y))
    try:
        print("divisão:",Dividir.Divisao.divisao("",x=int,y=int))
    except: ZeroDivisionError("não  é possivel dividir um numero por 0")
    print("multiplicação:",Multiplicar.Multiplicacao.multiplicacao("",x=int,y=int))
    print("raiz quadrada  de x:",Raizquadrada.RaizQuadrada.raizquadrada("",x=int))
print(Interacao.excute)