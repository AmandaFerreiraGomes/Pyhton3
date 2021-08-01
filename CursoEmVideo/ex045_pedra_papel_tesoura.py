""" Desafio 045: """


# importa-se a biblioteca random
import random


def linha():
	print('\033[34m', end='')
	print('-'*33)
	print('\033[m', end='')

def joquempo(choice_user, nome):
	L = ['PEDRA', 'PAPEL', 'TESOURA']  # tupla com as opcoes de jogo.
	
	choice_computer = random.choice(L)
	
	print(f'Computador: {choice_computer}'.upper())
	linha()
	
	if choice_computer == choice_user:
		print('Empate.'.upper())
	elif (choice_computer == 'PEDRA' and choice_user == 'PAPEL') or (choice_computer == 'TESOURA' and choice_user == 'PEDRA') \
			or (choice_computer == 'PAPEL' and choice_user == 'TESOURA'):
		print(f'{nome} Venceu!'.upper())
	elif (choice_computer == 'PAPEL' and choice_user == 'PEDRA') or (choice_computer == 'PEDRA' and choice_user == 'TESOURA') \
			or (choice_computer == 'TESOURA' and choice_user == 'PAPEL'):
		print('Computador Venceu!'.upper())


# Programa Principal:
if __name__ == '__main__':
	
	linha()
	print('\033[31m--------- JOQUEMPO v2.0.---------\033[m')
	linha()
	
	print('\033[36m', end='')
	nome = input('Digite seu nome: '.upper())
	print('\033[m', end='')
	
	linha()
	print('\033[34m', end='')
	choice_user = input('Digite Pedra, Papel ou Tesoura: '.upper()).upper()
	print('\033[m', end='')
	linha()

	joquempo(choice_user, nome)
	linha()


