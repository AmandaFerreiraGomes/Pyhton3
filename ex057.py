""" Desafio 057: """
# Programa Principal:


def main():
	sexo = ''
	while not(sexo == 'F' or sexo == 'M'):
		sexo = str(input('Sexo[F/M]: '))
	if sexo == 'M':
		print('Sexo: Masculino')
	elif sexo == 'F':
		print('Sexo: Feminino')
		

main()
