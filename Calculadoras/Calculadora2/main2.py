import operacoes.Dividir as Dividir
import operacoes.Multiplicar as Multiplicar
import operacoes.Raizquadrada as Raizquadrada
import operacoes.Somar as Somar
import operacoes.Subtrair as Subtrair
def main():
    """
    Docstring for main
    funcao que mostra  as operacoes da pasta operacoes apos introduzir dois numeros inteiros
    """
    print("Preciso que introduza dois valores:")
    x: int = int(input("x="))
    y: int = int(input("y="))

    # Teste
    # print(res)
    print("soma:",Somar.Soma.somar("",x,y))
    print("diferenca:",Subtrair.Diferenca.diferenca("",x,y))
    try:
        print("divisão:",Dividir.Divisao.divisao("",x,y))
    except: ZeroDivisionError("não  é possivel dividir um numero por 0")
    print("multiplicação:",Multiplicar.Multiplicacao.multiplicacao("",x,y))
    print("raiz quadrada  de x:",Raizquadrada.RaizQuadrada.raizquadrada("",x))
    

if __name__ == '__main__':
    main()
