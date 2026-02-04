import Substrair as sub
import Somar as som
import Dividir as div
import RaizQuadrada as rz
import Multiplicar as mult

def main():
    A=float(input("digite um numero: "))
    B=float(input("digite um numero: "))
    print("soma:",som.somar(A,B))
    print("dividir:",div.dividir(A,B))
    print("multiplicar:",mult.multiplicar(A,B))
    print("subtrair:",sub.subtrair(A,B))
    print("raiz quadrada:",rz.raizquadrada(A))
