""" Desafio 067: """
# Programa Principal:


def main():
	n = 0
	while True:
		print('-=' * 20)
		n = int(input('Digite um número: '))
		if n < 0:
			print('Programa Finalizado!')
			break
		y = f'TABUADA DE {n}'
		z = len(y) // 2
		print('-=' * z)
		print(y)
		print('-=' * z)
		for e in range(1, 10):
			print(f'{n} x {e} = {n*e}')
		print('Caso deseje sair, digite um valor negativo.')


main()
