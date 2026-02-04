import Calculadora2.operacoes.Dividir as Dividir,Calculadora2.operacoes.Subtrair as Subtrair,Calculadora2.operacoes.Somar as Somar,Calculadora2.operacoes.Multiplicar as Multiplicar,Calculadora2.operacoes.Raizquadrada as Raizquadrada 
def main():
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
    

if __name__ == '__main__':
    main()
