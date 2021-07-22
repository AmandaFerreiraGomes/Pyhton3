""" Desafio 095: """
# Programa Principal:


def main():
	cond = 'S'
	jogadores_dados = list()
	jogadores_dict = dict()
	golslista = list()
	texto = 'SISTEMA DE CADASTRO DE JOGADORES'
	j = (len(texto)//2) + 1
	print('\033[30:44m-=\033[m'*j)
	print(f'\033[7:30:44m {texto} \033[m')
	x = 0
	while True:
		totgols = 0
		medgols = 0
		if cond == 'S':
			print('\033[30:44m-=\033[m' * j)
			nome = str(input('\033[7:30:44m Nome:\033[m '))
			partidas = int(input('\033[7:30:44m Quantidade de Partidas Jogadas:\033[m '))
			jogadores_dict['Nome'] = nome
			jogadores_dict['Partidas'] = partidas
			for e in range(0, partidas):
				gols = int(input(f'\033[7:30:44mGols na Partida {e+1}:\033[m '))
				totgols = totgols + gols
				golslista.append(gols)
			medgols = totgols/partidas
			jogadores_dict['Média de Gols'] = medgols
			jogadores_dict['Gols'] = golslista[:]
			golslista.clear()
			jogadores_dict['Total de Gols'] = totgols
			jogadores_dados.append(jogadores_dict.copy())
			cond = str(input('\033[7:30:44m Deseja Continuar[S/N]?\033[m ')).upper()
		elif cond == 'N':
			print(jogadores_dados)
			print('\033[30:44m-=\033[m' * j)
			for e in jogadores_dados:
				print(f'{x} - ', end='')
				for k, v in e.items():
					print(f' {k} -> {v}')
				x = x + 1
			for v in jogadores_dados:
				print('\033[30:44m-=\033[m' * j)
				y = int(input('Digite o índice do jogador: '))
				while y > len(jogadores_dados)-1:
					print('ERRO! Jogador não cadastrado!')
					y = int(input('Digite o índice do jogador: '))
				print(f'{y} -> {jogadores_dados[y]}.')
			print('\033[30:44m-=\033[m' * j)
			print('\033[7:30:41m <<FINALIZADO!>> \033[m')
			break
		else:
			print('\033[1:30:41mCondição Inválida!\033[m')
			cond = str(input('Deseja Continuar[S/N]?')).upper()


main()
