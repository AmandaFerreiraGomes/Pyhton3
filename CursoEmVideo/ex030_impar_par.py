""" Desafio 030: """


def linha():
	print('-' * 30)


# Programa Principal:
if __name__ == "__main__":
	
	# solicita que o usuário digite um número, o qual será convertido para inteiro pela função int()
	linha()
	n = int(input('Digite um número: '))
	linha()
	
	# se o módulo(resto) do número dividido por dois for zero, então o número é par. Caso contrário, o número é ímpar.
	if n % 2 == 0:
		print(f'{n} é par!')
	else:
		print(f'{n} é ímpar!')
