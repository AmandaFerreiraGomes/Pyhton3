""" Desafio 001: """


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


def branco():
	cores = {
		'branco': '\033[30m'
	}
	return cores['branco']


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

print(f'{verde()}Olá, Mundo!')
print(f'{roxo()}Olá, Mundo!')

