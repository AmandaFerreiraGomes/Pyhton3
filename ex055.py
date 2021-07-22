""" Desafio 055: """
# Programa Principal:


def main():
	P = []
	for e in range(0, 5):
		peso = float(input(f'{e+1} - Digite seu peso(em kg): '))
		P.append(peso)
	print(f'Maior peso lido: {max(P)}kg\nMenor peso lido: {min(P)}kg')


main()
