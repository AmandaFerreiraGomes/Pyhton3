""" Desafio 031: """
# Programa Principal:


def main():
	print('-'*45)
	d = float(input('Digite a distância da viagem(em km): '))
	print('-'*45)
	if d <= 200.00:
		p = 0.50 * d
	else:
		p = 0.45 * d
	print(f'-> O valor da passagem é R$ \033[34m{p:.2f}')


main()
