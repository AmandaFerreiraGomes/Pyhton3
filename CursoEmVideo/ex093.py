""" Desafio 093: """
# Programa Principal:


def main():
	golslista = []
	dados = dict()
	dados['Nome'] = str(input('Nome: '))
	dados['Partidas'] = int(input('Quantidade de Partidas Jogadas: '))
	totgols = 0
	for p in range(0, dados['Partidas']):
		gols = int(input(f'Gols feitos na partida {p+1}: '))
		totgols = totgols + gols
		golslista.append(gols)
	dados['Gols'] = golslista
	dados['Total de Gols'] = totgols
	print('------DADOS COLETADOS------')
	for k, v in dados.items():
		print(f'{k} -> {v}')


main()
