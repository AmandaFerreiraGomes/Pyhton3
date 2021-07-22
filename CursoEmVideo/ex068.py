""" Desafio 068: """
from random import randint
from emoji import *
# Programa Principal:


def main():
	s = 'JOGO DE PAR OU ÍMPAR'
	print('-='*(len(s)//2))
	print(s)
	print('-=' * (len(s) // 2))
	choice_comp = choice_user = 0
	x = y = 0
	while True:
		choice_comp = randint(0, 10)
		choice_user = int(input('Digite um número: '))
		som = choice_user + choice_comp
		print('-='*15)
		if (som % 2 == 0 and choice_user % 2 == 0) or (som % 2 != 0 and choice_user % 2 != 0):
			print(f'Você Venceu!\nComputador: {choice_comp}\nVocê: {choice_user}\nSoma: {som}.')
			x = x + 1
		elif (choice_comp%2==0 and choice_user%2==0) or (choice_comp % 2 != 0 and choice_user % 2 != 0):
			print(f'EMPATE!\nCOMPUTADOR: {choice_comp}\nVOCÊ: {choice_user}\nSOMA: {som}.')
			y = y +1
		else:
			print(f'Você Perdeu!\nComputador: {choice_comp}\nVocê: {choice_user}\nSoma: {som}')
			break
		print('-=' * 15)
	print(f'Total de Vitórias Conquistadas: {x}.\nTotal de Empates: {y}.')
	

main()
