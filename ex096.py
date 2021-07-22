""" Desafio 096: """
# Funções Personalizadas:


def area(a, b):
	return a * b


# Programa Principal:


def main():
	largura = float(input('Largura(m): '))
	comprimento = float(input('Comprimento(m): '))
	arearet = area(largura, comprimento)
	print(f'Área: {largura} x {comprimento} = {arearet} m2.')


main()
