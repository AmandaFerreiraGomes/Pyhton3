""" Desafio 049: """
# Programa Principal:


def main():
	n = int(input('Digite um número: '))
	print(f'----------Tabuada de {n}----------')
	for e in range(0, 11):
		print(f'{n} + {e} = {n + e}')


main()
