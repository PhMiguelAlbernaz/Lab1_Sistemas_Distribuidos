import operacoes.Dividir as Dividir
import operacoes.Multiplicar as Multiplicar
import operacoes.Raizquadrada as Raizquadrada
import operacoes.Somar as Somar
import operacoes.Subtrair as Subtrair
def main():
    while True:
        opacao:int = int(input("digite a  opcao que deseja(1-somar,2-subtrair,3-dividir," \
        "4-multiplicar,5-raiz quadrada):"))
        match opacao:
            case 1:
                A:int =int(input("digite um numero:"))
                B:int =int(input("digite um numero:"))
                print(Somar.Soma.somar("",A,B))
            case 2:
                A=int(input("digite um numero:"))
                B=int(input("digite um numero:"))
                print(Subtrair.Diferenca.diferenca("",A,B))
            case 3:
                A=int(input("digite um numero:"))
                B=int(input("digite um numero:"))
                try:
                    print(Dividir.Divisao.divisao("",A,B))
                except:ZeroDivisionError("erro")
            case 4:
                A=int(input("digite um numero:"))
                B=int(input("digite um numero:"))
                print(Multiplicar.Multiplicacao.multiplicacao("",A,B))
            case 5:
                A=int(input("digite um numero:"))
                print(Raizquadrada.RaizQuadrada.raizquadrada("",A))
            case 0:
                exit()
            case _:
                return main() 
if __name__ == '__main__':
    main()
