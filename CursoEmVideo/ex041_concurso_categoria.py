""" Desafio 041: """


def linha():
	print('-' * 32)


# Programa Principal:


if __name__ == "__main__":
	
	# solicita que o usuário entre com seu ano de nascimento para saber qual é a categoria dele no concurso.
	ano = int(input('Digite seu ano de nascimento: '))
	
	# calcula-se a idade, baseado no ano atual, que é 2021
	idade = 2021 - ano
	
	# interação com o usuário com o cabeçalho abaixo
	linha()
	print('\033[34m---------- CATEGORIA -----------\033[m')
	linha()
	
	# exibe a idade em anos do concorrente
	print(f'Idade: {idade} anos.')
	
	# se a idade for menor ou igual a 9, o concorrente é enquadrado como candidato mirim
	if idade <= 9:
		print('Mirim.')
	# caso seja menor ou igual a 14, ele é enquadrado como infantil
	elif idade <= 14:
		print('Infantil.')
	# se for menor ou igual a 19, ele se enquadra como júnior
	elif idade <= 19:
		print('Júnior.')
	# caso a idade seja exatamente 20 anos, ele é sênior
	elif idade == 20:
		print('Sênior.')
	# acima de 20 anos é master
	else:
		print('Master.')
	
