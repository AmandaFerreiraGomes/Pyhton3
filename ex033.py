""" Desafio 033: """


def azul():
	cores = {
		'azul': '\033[34m'
	}
	return cores['azul']


# Programa Principal:
print(f'{azul()}-'*30)
a = int(input('Digite um número: '))
b = int(input('Digite outro: '))
c = int(input('Digite o último: '))
print(f'{azul()}-'*30)
menor = a
maior = b
if b < a and c < a:
	maior = a
if b < c and a < c:
	maior = c
if b < a  and b < c:
	menor = b
if c < a and c < b:
	menor = c
print(f'Maior: {maior}\nMenor: {menor}')
print(f'{azul()}-'*30)
