""" Desafio 019: """
from random import choice

# Programa Principal
print('-' * 30)
print('		SORTEIO')
print('-' * 30)
n1 = input('Digite o nome do aluno 1: ')
n2 = input('Digite o nome do aluno 2: ')
n3 = input('Digite o nome do aluno 3: ')
n4 = input('Digite o nome do aluno 4: ')
L = [n1, n2, n3, n4]
sort = choice(L)
print(f'O aluno sorteado foi: {sort}.')
