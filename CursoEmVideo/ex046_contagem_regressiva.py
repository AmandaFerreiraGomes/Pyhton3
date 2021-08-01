""" Desafio 046: """

from time import sleep 
from emoji import emojize


def contagem(): # contagem regressiva para a virada do ano (são dez segudos).
	for e in range(10, 0, -1):
		print(f'{e}')
		sleep(1) # utiliza-se a função sleep importada da biblioteca time para fazer a contagem de diminuição de ums segundo por loop do for.


def linha():
	print('-'*48)

if __name__ == "__main__":
	
	try:
		linha()
		print('--- CONTAGEM REGRESSIVA PARA A VIRADA DO ANO ---')
		linha()
		contagem()
		print(4*emojize(':fireworks:'))
	except (KeyboardInterrupt, ValueError, KeyError):
		print('\033[31mErro!\033[m')
