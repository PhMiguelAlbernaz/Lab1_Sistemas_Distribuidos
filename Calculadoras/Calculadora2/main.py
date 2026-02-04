import Calculadora2.operacoes.Dividir as Dividir,Calculadora2.operacoes.Subtrair as Subtrair,Calculadora2.operacoes.Somar as Somar,Calculadora2.operacoes.Multiplicar as Multiplicar,Calculadora2.operacoes.Raizquadrada as Raizquadrada 
def main():
    while True:
        opacao = int(input("digite a  opcao que deseja(1-somar,2-subtrair,3-dividir," \
        "4-multiplicar,5-raiz quadrada):"))
        match opacao:
            case 1:
                A=int(input("digite um numero:"))
                B=int(input("digite um numero:"))
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
                print(Multiplicar.multiplicacao.multiplicacao("",A,B))
            case 5:
                A=int(input("digite um numero:"))
                print(Raizquadrada.RaizQuadrada.raizquadrada("",A))
            case 0:
                exit()
            case _:
                return main() 
if __name__ == '__main__':
    main()
