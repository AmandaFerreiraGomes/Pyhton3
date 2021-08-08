""" Desafio 053: """


def linha():
	print('-'*43)


def red():
	print('\033[31m')


def blue():
	print('\033[34m')


def black():
	print('\033[m')


# Programa Principal:
def main():
	
	# cabeçalho.
	linha()
	print(' PALINDROMO '.center(43, '-'))
	linha()
	
	# entrada de uma frase, em que todos os caracteres serão transformados em caixa alta e os espaços serão removidos.
	frase = str(input('Digite uma frase: ')).strip().upper()
	
	# lista palavras recebe todos os caracteres os quais são separados um a um.
	palavras = frase.split()
	
	# remove-se os espaços com o uso da função replace.
	junto = frase.replace(' ', '')
	
	# inverso recebe a frase com todos os caracteres juntos, começando a contar do último até o primeiro, um a um
	inverso = junto[::-1]
	
	# for letra in range(len(junto)-1, -1, -1):
	# ...inverso = inverso + junto[letra]
	
	linha()
	# exibe-se o resultado
	print(f'Frase: {frase}')
	print(f'Inverso: {inverso}')
	
	linha()
	if inverso == junto:
		blue()
		print('A frase digitada é um palíndromo!'.center(43, ' '))
		black()
	else:
		red()
		print(f'A frase digitada não é um palíndromo!'.center(43, ' '))
		black()
	linha()


if __name__ == '__main__':
	main()
