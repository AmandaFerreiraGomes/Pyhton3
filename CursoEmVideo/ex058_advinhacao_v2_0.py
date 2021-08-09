""" Desafio 058: """


from random import randint


def linha():
	print('-' * 50)


# Programa Principal:
def main():
	
	# cabeçalho.
	linha()
	print(' Jogo da Adivinhação 2.0 '.center(50, '-'))
	linha()
	
	# o número sorteado é escolhido e fica entre 0 e 9.
	n = randint(0, 10)
	
	# inicializa-se a variavel x, a qual será utilizada como contador do número de tentativas.
	x = 0
	
	# inicializa-se num com 11 por estar fora da abrangência de n.
	num = 11
	
	# enquanto num for diferente de n, o usuário poderá chutar o valor.
	while num != n:
		num = int(input('Digite um número entre 0 e 10: '))
		x = x + 1
	
	# exibe-se o resultado e a quantidade de tentativas.
	linha()
	print(f'O número sorteado foi {n}.\nVocê precisou de {x} tentativas para encontrá-lo.')
	linha()


if __name__ == '__main__':
	main()
