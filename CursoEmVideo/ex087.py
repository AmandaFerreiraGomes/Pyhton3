""" Desafio 087: """
# Programa Principal:


def main():
	lista1 = []
	lista2 = []
	s = s2 = 0
	for i in range(0, 3):
		for j in range(0, 3):
			num = int(input(f'[{i}][{j}] - Digite um número: '))
			if num % 2 == 0:
				s = s + num
			if i == 1:
				lista2.append(num)
			if j == 2:
				s2 = s2 + num
				lista1.append(num)
	print(f'Soma de todos os valores pares: {s}.')
	print(f'A soma de todos os valores da terceira coluna: {s2}')
	print(f'O maior valor da segunda linha: {max(lista2)}')
	


main()
