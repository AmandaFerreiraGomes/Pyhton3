def azul():
	cores = {
		'azul': '\033[34m'
	}
	return cores['azul']


def amarelo():
	cores = {
		'amarelo': '\033[33m',
		'ciano': '\033[36m',
		'cinza': '\033[37m'
	}
	return cores['amarelo']


def vermelho():
	cores = {
		'vermelho': '\033[31m',
	}
	return cores['vermelho']


def verde():
	cores = {
		'verde': '\033[32m',
	}
	return cores['verde']


def roxo():
	cores = {
		'roxo': '\033[35m',
	}
	return cores['roxo']


# Programa Principal:
if __name__ == "__main__":
	print(f'{verde()}Olá, Mundo!')
	print(f'{roxo()}Olá, Mundo!')
	print(f'{vermelho()}Olá, Mundo!')
	print(f'{amarelo()}Olá, Mundo!')
	print(f'{azul()}Olá, Mundo!')
