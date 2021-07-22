""" Desafio 020: """
from random import shuffle

# Programa Principal
print('-' * 30)
print('		SEQUÊNCIA DO SORTEIO')
print('-' * 30)
n1 = input('Digite o nome do aluno 1: ')
n2 = input('Digite o nome do aluno 2: ')
n3 = input('Digite o nome do aluno 3: ')
n4 = input('Digite o nome do aluno 4: ')
L = [n1, n2, n3, n4]
s = shuffle(L)
print(f'A ordem de sorteio foi {L}.')

