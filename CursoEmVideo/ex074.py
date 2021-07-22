""" Desafio 074: """
from random import randint
# Programa Principal:


def main():
	lst = []
	x = 0
	while x < 5:
			if x == 5:
				break
			c = randint(0, 100)
			lst.append(c)
			x = x + 1
	tupla = tuple(lst)
	maior = max(tupla)
	menor = min(tupla)
	print(f'Os valores sorteados foram: {str(tupla)}')
	print(f'Maior: {maior} e Menor: {menor}')
	

main()
