""" Desafio 049: """
# Programa Principal:


def linha():
	print('-'*34)


def main():
	
	# inserção de dados pelo usuário
	linha()
	n = int(input('Digite um número: '))
	
	# cabeçalho.
	linha()
	print(f'---------- Tabuada de {n} ----------')
	linha()
	
	# laço que calcula e exibe o resultado da tabela de soma de 'n'.
	# para e no intervalo [0, 10], com e iniciando com zero.
	for e in range(0, 11):
		print(f'{n} + {e} = {n + e}')
	
	linha()


if __name__ == '__main__':
	main()

