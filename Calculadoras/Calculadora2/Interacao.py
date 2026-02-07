import Calculadoras.Calculadora2.operacoes.Dividir as Dividir
import Calculadoras.Calculadora2.operacoes.Multiplicar as Multiplicar
import Calculadoras.Calculadora2.operacoes.Raizquadrada as Raizquadrada
import Calculadoras.Calculadora2.operacoes.Somar as Somar
import Calculadoras.Calculadora2.operacoes.Subtrair as Subtrair
class Interacao:
    def excute(self):
        print("Preciso que introduza dois valores:")
    x: int = int(input("x="))
    y: int = int(input("y="))

    # Teste
    # print(res)
    print("soma:",Somar.Soma(x,y).soma)
    print("diferenca:",Subtrair.Diferenca(x,y).diferenca)
    try:
        print("divisão:",Dividir.Divisao(x,y).divisao)
    except: ZeroDivisionError("não  é possivel dividir um numero por 0")
    print("multiplicação:",Multiplicar.Multiplicacao(x,y).multiplicacao)
    print("raiz quadrada  de x:",Raizquadrada.RaizQuadrada(x).raizquadrada)
print(Interacao.excute)