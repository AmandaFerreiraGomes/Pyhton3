""" Desafio 048: """
import emoji
# Programa Principal:


def main():
	print('\033[34mÍmpares múltiplos de 3 que se encontram no intervalo [1, 500].\033[m')
	soma = 0
	for e in range(1, 500):
		if (e % 2 != 0) and (e % 3 == 0):
			impar = e
			soma = soma + e
			print('->', impar)
	print(f'Soma: {soma}')
	print(emoji.emojize(':sunglasses:'))

	
main()
