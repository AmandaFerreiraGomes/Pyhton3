""" Desafio 037: """
# Programa Principal:


def main():
	num = int(input('Digite um número inteiro qualquer: '))
	conversao = 0
	print("""ESCOLHA A BASE DE CONVERSÃO:
			1 - BINÁRIO
			2 - OCTAL
			3 - HEXADECIMAL""")
	b = int(input(''))
	if b == 1:
		conversao = bin(num)
	elif b == 2:
		conversao = oct(num)
	elif b == 3:
		conversao = hex(num)
	else:
		print('Opção Inválida! Escolha entre 1, 2 e 3.')
	print(f'{conversao[2:]}'.upper())


main()
