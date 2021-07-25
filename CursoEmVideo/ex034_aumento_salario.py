""" Desafio 034: """

# função que retorna a cor azul, para os caracteres
def azul():
	return '\033[34m'

# função que retorna a cor branca para os caracteres. em telas brancas, o pycharm coloca a cor em preto
def branco():
	return '\033[30m'

# função que define uma linha com 30 caracteres '-' na cor azul
def linha_azul():
	print(f'{azul()}-'*30)


# Programa Principal:
if __name__ == "__main__":
	
	# solicita que o usuário digite o valor do salário
	linha_azul()
	salario = float(input('Qual o valor do seu salário? R$ '))
	
	# com base no valor digitado pelo usuário, verifica-se a condição de o salário ser maior que R$ 1250,00. Se for maior, então o novo salário(n_s) terá um aumento de 10%
	# caso seja menor que R$ 1250,00, então o novo salário terá um aumento de 15%.
	if salario > 1250.00:
		n_s = salario + (salario * 0.10)
	else:
		n_s = salario + (salario * 0.15)
	linha_azul()
	
	# exibe os resultados do programa
	print(f'{branco()}Novo salário: R$ {n_s:.2f}. Aumento: R$ {n_s-salario:.2f}.')
