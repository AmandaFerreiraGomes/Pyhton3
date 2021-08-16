""" Desafio 060: """


from math import factorial


def linha():
	print('-' * 30)

	
# Programa Principal:
def main():
	
	# entrada de dados.
	linha()
	f = int(input('Digite um número: '))
	
	c = f
	fat = factorial(f)
	
	# cabeçalho do resultado.
	linha()
	print(f' FATORIAL DE {f}! '.center(30))
	linha()
	
	# enquanto o valor digitado for maior que 1
	while c >= 1:
		# se c for igual a 1, então imprima c e o fatorial de c.
		if c == 1:
			print(f' {c} = {fat}')
		# caso contrário imprima 'c x' sem quebra de linha.
		else:
			print(f' {c} x', end='')
		# c é decrementado a cada nova repetição.
		c = c - 1
		
	
if __name__ == '__main__':
	main()
