""" Desafio 016: """


# importando da biblioteca math a função trunc(), a qual realiza o truncamento de um determinado número, retornando a parte inteira do mesmo. 
# Exemplo: 5.32 quando truncando = 5
from math import trunc


# Programa Principal:
if __name__ == "__main__":
  
    # usuário insere o valor que deseja truncar
    num = float(input('Digite um número: '))
    
    # exibição do valor truncado
    print(f'O número {num} tem a parte inteira {trunc(num)}')
