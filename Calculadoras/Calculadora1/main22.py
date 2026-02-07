import Calculadoras.Calculadora1.Substrair as sub
import Calculadoras.Calculadora1.Somar as som
import Calculadoras.Calculadora1.Dividir as div
import Calculadoras.Calculadora1.RaizQuadrada as rz
import Calculadoras.Calculadora1.Multiplicar as mult

def main():
    A=float(input("digite um numero: "))
    B=float(input("digite um numero: "))
    print("soma:",som.somar(A,B))
    print("dividir:",div.dividir(A,B))
    print("multiplicar:",mult.multiplicar(A,B))
    print("subtrair:",sub.subtrair(A,B))
    print("raiz quadrada:",rz.raizquadrada(A))
