""" Desafio 057: """


def linha():
	print('-'*20)


# Programa Principal:
def main():
	
	# inicializa-se a variável sexo
	sexo = ''
	
	linha()
	# enquanto sexo for diferente de F ou M, o programa continua a pedir que o usuário digite o sexo.
	while not (sexo == 'F' or sexo == 'M'):
		sexo = str(input('Sexo[F/M]: ')).upper()
	linha()
	# se sexo for m, exibe masculino.
	if sexo == 'M':
		print('Sexo: Masculino'.center(20))
	# caso seja f, exibe-se feminino.
	elif sexo == 'F':
		print('Sexo: Feminino'.center(20))
	linha()


if __name__ == '__main__':
	main()

