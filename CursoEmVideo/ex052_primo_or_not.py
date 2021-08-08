""" Desafio 052: """


def linha():
	print('-'*45)


# Programa Principal:
def main():
	
	# cabecalho.
	linha()
	print('---- Valores primos no intervalo [1, 99] ----')
	linha()
	
	# para e no intervalo de [1, 99].
	for e in range(1, 100):
		
		# n recebe e.
		n = e
		
		# não é primo.
		primo = False
		
		# verifica se n é primo.
		if n > 1 and (not (n > 2 and n % 2 == 0)) and (not (n > 3 and n % 3 == 0)) and (not (n > 5 and n % 5 == 0)) and (
				not (n > 7 and n % 7 == 0)):
			primo = True
		
		# se primo for True, então exibe a mensagem de que n é primo.
		if primo:
			print(f'{n} é primo!'.center(45))
		# caso contrário, exibe a mensagem de que n não é primo.
		else:
			print(f'{n} não é primo!'.center(45))
	
	linha()
	# centralize a string, com 45 espaços preenchidos pelo caractere -.
	print(' FIM! '.center(45, '-'))
	
	linha()


if __name__ == '__main__':
	main()


"""Números maiores que 1, divisíveis apenas por 1 e por eles mesmos, não divisíveis por 2, além do próprio 2."""

