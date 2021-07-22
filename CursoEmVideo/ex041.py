""" Desafio 041: """
# Programa Principal:


def main():
	ano = int(input('Digite seu ano de nascimento: '))
	idade = 2020 - ano
	print('\033[30:44m----------CATEGORIA-----------\033[m')
	print(f'Idade: {idade} anos.')
	if idade <= 9:
		print('Mirim.')
	elif idade <= 14:
		print('Infantil.')
	elif idade <= 19:
		print('Júnior.')
	elif idade == 20:
		print('Sênior.')
	else:
		print('Master.')
	
	
main()
