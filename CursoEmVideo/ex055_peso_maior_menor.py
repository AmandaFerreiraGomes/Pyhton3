""" Desafio 055: """


def linha():
	print('-'*30)


# Programa Principal:
def main():
	
	linha()
	print('PESQUISA DE PESO(Kg)'.center(30))
	linha()
	
	# inicializa-se a lista p vazia.
	p = []
	
	# 5 valores serão inseridos pelo usuário e posteriormente cada um é inserido na lista p.
	for e in range(0, 5):
		peso = float(input(f'{e+1} - Digite seu peso(em kg): '))
		p.append(peso)
	
	# exibe-se o resultado da pesquisa, em que aparecem o maior e o menor peso inseridos.
	# as funções built-in max() e min() são utilizadas.
	linha()
	print(f'Maior peso lido: {max(p)}kg\nMenor peso lido: {min(p)}kg'.center(30))
	linha()


if __name__ == '__main__':
	main()
