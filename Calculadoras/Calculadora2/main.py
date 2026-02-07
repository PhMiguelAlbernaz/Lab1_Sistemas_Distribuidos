import Calculadoras.Calculadora2.operacoes.Dividir as Dividir
import Calculadoras.Calculadora2.operacoes.Multiplicar as Multiplicar
import Calculadoras.Calculadora2.operacoes.Raizquadrada as Raizquadrada
import Calculadoras.Calculadora2.operacoes.Somar as Somar
import Calculadoras.Calculadora2.operacoes.Subtrair as Subtrair
def main():
    while True:
        opacao:int = int(input("digite a  opcao que deseja(1-somar,2-subtrair,3-dividir," \
        "4-multiplicar,5-raiz quadrada):"))
        match opacao:
            case 1:
                A:int =int(input("digite um numero:"))
                B:int =int(input("digite um numero:"))
                print(Somar.Soma(A,B).soma)
            case 2:
                A=int(input("digite um numero:"))
                B=int(input("digite um numero:"))
                print(Subtrair.Diferenca(A,B).diferenca)
            case 3:
                A=int(input("digite um numero:"))
                B=int(input("digite um numero:"))
                try:
                    print(Dividir.Divisao(A,B).divisao)
                except:ZeroDivisionError("erro")
            case 4:
                A=int(input("digite um numero:"))
                B=int(input("digite um numero:"))
                print(Multiplicar.Multiplicacao(A,B).multiplicacao)
            case 5:
                A=int(input("digite um numero:"))
                print(Raizquadrada.RaizQuadrada(A).raizquadrada)
            case 0:
                exit()
            case _:
                return main() 
if __name__ == '__main__':
    main()
