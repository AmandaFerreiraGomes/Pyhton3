""" Desafio 048: """
import emoji


def linha():
	print('-'*66)


# Programa Principal:
def main():
	
	# cabecalho.
	linha()
	print('\033[34m  Ímpares múltiplos de 3 que se encontram no intervalo [1, 500].  \033[m')
	linha()
	
	# inicializa-se a variável soma.
	soma = 0
	
	for e in range(1, 501):
		if (e % 2 != 0) and (e % 3 == 0):
			impar = e
			soma = soma + e
			print('->', impar)
	
	# resultado da soma de todos os valores ímpares múltiplos de 3, os quais se encontram no intervalo fechado [1, 500].
	print(f'Soma: {soma}')
	
	# mostra um emoji de óculos de sol.
	print(emoji.emojize(':sunglasses:'))


if __name__ == '__main__':
	main()

