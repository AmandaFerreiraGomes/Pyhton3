""" Desafio 031: """
# Programa Principal:

def linha():
	print('-' * 45)


if __name__ == "__main__":
	
	# solicita q o usuário insira a quantidade de kms percorridos na viagem
	linha()
	d = float(input('Digite a distância da viagem(em km): '))
	linha()
	
	# caso a distância percorrida seja menor ou igual a 200 km, o km da passagem custará R$ 0.50. Caso a distância seja maior que 200, o km custará R$ 0,45.
	if d <= 200.00:
		p = 0.50 * d
	else:
		p = 0.45 * d
		
	# exibe o valor da passagem na cor roxa
	print(f'-> O valor da passagem é R$ \033[35m{p:.2f}')
