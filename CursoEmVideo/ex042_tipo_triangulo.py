""" Desafio 042: """


def linha():
	print('-' * 34)


# Programa Principal:
if __name__ == "__main__":
	
	# cabeçalho:
	linha()
	print('------- SERÁ UM TRIâNGULO? -------')
	linha()
	
	# inserção de dados
	a = int(input('Digite o valor do cateto: '))
	b = int(input('Digite o valor do outro cateto: '))
	c = int(input('Digite o valor de outro cateto: '))
	linha()
	
	# faz a verificação se o triângulo pode ser formado por esses três segmentos de reta
	if (abs(b-c) < a < b + c) and (abs(a-c) < b < a + c) and (abs(a - b) < c < a + b):
		# exibe a mensagem de que é possível que esses três segmentos de reta formem um triângulo
		print(f'Os segmentos {a}, {b} e {c} podem formar um TRIâNGULO!')
		
		# se todos os lados forem iguais, então o triângulo é equilátero
		if a == b and b == c:
			print('Triângulo Equilátero.')
		# se todos os lados forem diferentes, então o triângulo é escaleno
		elif a != b and b != c and a != c:
			print('Triângulo Escaleno.')
		# por último, tem-se o isóceles, no qual dois lados são iguais.
		else:
			print('Triângulo Isósceles.')
	# caso não seja possível que os três segmentos formem um triângulo, exibe-se a mensagem abaixo
	else:
		print('Os segmentos não podem formar um TRIÂNGULO!')
	
	linha()

