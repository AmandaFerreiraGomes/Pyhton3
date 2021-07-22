""" Desafio 028: """
from random import randint
# Programa Principal:
x = randint(0, 5)
num = int(input('Digite um número inteiro(0 a 5): '))
if num == x:
	print('VOCÊ VENCEU!')
else:
	print('VOCÊ PERDEU')
print(f'O número sorteado foi {x}')
