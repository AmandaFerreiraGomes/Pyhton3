
""" Desafio 002: """


def azul():
	cores = {
		'azul': '\033[34m'
	}
	return cores['azul']

def main():
	a = input('Digite seu nome: ')
	print(f'É um prazer te conhecer, {azul()}{a}!')


main()
