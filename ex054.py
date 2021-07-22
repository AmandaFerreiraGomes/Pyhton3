""" Desafio 054: """
# Programa Principal:


def main():
	x = 0
	y = 0
	for e in range(0,7):
		ano = int(input('Digite seu ano de nascimento: '))
		idade = 2020 - ano
		if idade >= 21:
			x = x + 1
		else:
			y = y + 1
	print(f'{x} pessoas têm idade igual ou superior a 21 anos e {y} pessoas têm menos de 21 anos.')
	
	
main()
