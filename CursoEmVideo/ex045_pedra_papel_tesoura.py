""" Desafio 045: """


# importa-se a biblioteca random
import random


def linha():
	print()


# Programa Principal:
def main():
	nome = str(input('Digite seu nome: '))
	L = ['Pedra', 'Papel', 'Tesoura']
	choice_computer = random.choice(L)
	choice_user = str(input('Digite Pedra, Papel ou Tesoura.'))
	print(f'Computador: {choice_computer}')
	if choice_computer == choice_user:
		print('Empate.')
	elif (choice_computer == 'Pedra' and choice_user == 'Papel') or (choice_computer == 'Tesoura' and choice_user == 'Pedra') or (choice_computer == 'Papel' and choice_user == 'Tesoura'):
		print(f'{nome} Venceu!')
	elif (choice_computer == 'Papel' and choice_user == 'Pedra') or (choice_computer == 'Pedra' and choice_user == 'Tesoura') or (choice_computer == 'Tesoura' and choice_user == 'Papel'):
		print('Computador Venceu!')

	
main()
