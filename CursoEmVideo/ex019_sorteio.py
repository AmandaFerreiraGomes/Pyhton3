""" Desafio 019: """


# importa-se da biblioteca random a função choice, a qual permite a escolha de um número de qualquer sequência que quisermos.
from random import choice


def linha():
    print('-' * 30)
    
    
# Programa Principal
if __name__ == "__main__":
    
    # cabeçalho
    linha()
    print('		SORTEIO')
    linha()
    
    # inserção dos valores que farão parte da tupla de possíveis escolhas para choice.
    n1 = input('Digite o nome do aluno 1: ')
    n2 = input('Digite o nome do aluno 2: ')
    n3 = input('Digite o nome do aluno 3: ')
    n4 = input('Digite o nome do aluno 4: ')
    linha()
    
    # atribuição da tupla
    L = [n1, n2, n3, n4]
    
    # a variável sort recebe o resultado da escolha feita pela função choice
    sort = choice(L)
    
    # exibe-se o resultado do sorteio
    print(f'O aluno sorteado foi: {sort}.')
