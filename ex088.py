""" Desafio 088: """
import random
# Programa Principal:


def main():
	mega = 'JOGO DA MEGA-SENA'
	stri = ('-'*(len(mega)+10))
	print(f'{stri:^}')
	print(f'{mega:^25}')
	print(f'{stri:^}')
	lista = []
	sorteio = []
	for e in range(1, 61):
		lista.append(e)
	while True:
		qtd_jogos = int(input('-> Quantos jogos você deseja fazer? (0 para finalizar) '))
		if qtd_jogos == 0:
			print('Programa Finalizado!')
			break
		else:
			for e in range(0, qtd_jogos):
				s = random.sample(lista, 5)
				s.sort()
				sorteio.append(s[:])
			print(f'Sequência de {e+1} jogos: {sorteio}.')
			print()

	

main()

