""" Desafio 091: """
from random import randint
from operator import itemgetter
from time import sleep


# Programa Principal:


def main():
	lista = []
	sorteio = {'jogador 1': randint(1, 6), 'jogador 2': randint(1, 6),
			'jogador 3': randint(1, 6), 'jogador 4': randint(1, 6)}
	ranking = dict()
	ranking = sorted(sorteio.items(), key=itemgetter(1), reverse=True)
	print('-> VALORES SORTEADOS:')
	for k, v in sorteio.items():
		print(f'{k}: {v}.')
	print('-------------RANKING-------------')
	for k, v in enumerate(ranking):
		if k == 0:
			print(f'-> Vencedor: {v[0]}.')
		print(f'{k+1}º - {v[0]} tirou {v[1]} no dado.')
		sleep(1)
	print('PROGRAMA FINALIZADO!')


main()
