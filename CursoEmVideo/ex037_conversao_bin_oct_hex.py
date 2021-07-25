""" Desafio 037: """


def linha():
	print('-' * 40)


# Programa Principal:
if __name__ == "__main__":
	
	# a variavel num recebe o valor digitado pelo usuário
	linha()
	num = int(input('Digite um número inteiro qualquer: '))
	linha()
	conversao = 0 # inicializa a variável conversão, para ajudar a identificar quais variáveis serão utilizadas durante o programa. Considero uma boa prática.
	
	# exibição do menu de escolhas, para qual base numérica o usuário vai querer converter o número digitado
	print("""ESCOLHA A BASE DE CONVERSÃO:
			1 - BINÁRIO
			2 - OCTAL
			3 - HEXADECIMAL""")
	
	# entra-se com a opção para a qual se deseja converter
	linha()
	b = int(input('Opção escolhida: '))
	linha()
	
	# se b for 1 a conversão é para a base binária(0 ou 1) 
	if b == 1:
		conversao = bin(num)
	# se b for 2, então a conversão é para a base octal (0 a 7)
	elif b == 2:
		conversao = oct(num)
	# se b for 3, então a conversão será para a base hexadecimal (0 a 9, A(10), B(11), C(12), D(13), E(14), F(15))
	elif b == 3:
		conversao = hex(num)
	# opção de proteção para o caso de haver alguma inserção fora do intervalo definido no menu
	else:
		print('Opção Inválida! Escolha entre 1, 2 e 3.')
		
	# caso tenha letra, a mesma ficará maiúscula. Exibe-se o resultado.
	print(f' Resultado: {conversao[2:]}'.upper())
	linha()

