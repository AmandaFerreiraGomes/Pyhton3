""" Desafio 058: """
import random
# Programa Principal:


def main():
	print('-----Jogo da Adivinhação 2.0-----')
	n = random.randint(0, 10)
	x = 0
	num = 11
	while num != n:
		num = int(input('Digite um número entre 0 e 10: '))
		x = x + 1
	print(f'O número sorteado foi {n}. Você precisou de {x} tentativas para encontrá-lo.')


main()
