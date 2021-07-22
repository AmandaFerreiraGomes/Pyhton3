""" Desafio 073: """
# Programa Principal:


def main():
	brasileirao = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico - PR', 'São Paulo', 'Internacional',
				'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco', 'Atlético - MG', 'Fluminense', 'Botafogo',
				'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')
	for c in range(0, 5):
		print(f'{c+1}º - {brasileirao[c]}')
	for e in range(16, len(brasileirao)):
		print(f'{e+1}º - {brasileirao[e]}')
	print(sorted(brasileirao))
	x = 'Chapecoense'
	p = brasileirao.index(x)
	print(f'Chapecoense está na {p+1}º posição.')


main()
