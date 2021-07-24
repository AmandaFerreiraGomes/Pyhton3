""" Desafio 018: """


# importando da biblioteca math as funções seno, cosseno e tangente.
from math import sin, cos, tan

def linha():
    print('-' * 30)

    
# Programa Principal: o usuário insere a medida de um ângulo e o programa retorna os valores do seno, do cosseno e da tangente do referido ângulo.
if __name__ == "__main__":
  
    linha()
    # definição do ângulo que será base para a execução dos cálculos de sin, cos e tan
    a = int(input('Digite a medida do ângulo em radianos: '))
    
    # exibição do resultado dos cálculos
    linha()
    print(f'-> Seno: {sin(a):.2f}\n-> Cosseno: {cos(a):.2f}\n-> Tangente: {tan(a):.2f}.')
    linha()
