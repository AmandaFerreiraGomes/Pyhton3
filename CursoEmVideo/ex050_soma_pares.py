""" Desafio 050: """
# Programa Principal:


def linha():
	print('-'*32)


def main():
	
	s = 0
	
	linha()
	print('-------- Soma dos Pares --------')
	linha()
	
	# dentro do laço são solicitadas seis entradas de números, dos quais será calculada a soma
	# total dos valores que são pares.
	for e in range(0, 6):
		
		n = int(input(f'Digite o {e + 1} número: '))
		# se n for divisível por 2, então é calculada a soma com n.
		if n % 2 == 0:
			s = s + n
	
	linha()
	
	# exibe-se o resultado da soma dos valores inseridos que são pares.
	print(f'Soma: {s}')
	linha()


if __name__ == '__main__':
	main()
	
