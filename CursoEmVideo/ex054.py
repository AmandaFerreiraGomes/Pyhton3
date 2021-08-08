""" Desafio 054: """


import datetime


def linha():
	print('-'*60)


# Programa Principal:
def main():
	
	# inicializa-se as variáveis que serão utilizadas no programa.
	x = 0
	y = 0
	ano_atual = 0
	idade = 0
	
	# usa-se a biblioteca datetime para utilizar o ano de atual vigência no programa.
	atual_date_time = datetime.datetime.now()
	data = atual_date_time.date()
	ano_atual = int(data.strftime("%Y"))
	
	# cabeçalho.
	linha()
	print('PESQUISA DE FAIXA ETÁRIA'.center(60))
	linha()
	print(f'Ano atual: {ano_atual}'.center(60))
	linha()
	
	# 7 loops.
	for e in range(1, 8):
		# requisita que o usuário digite o ano de nascimento.
		ano = int(input('\tDigite seu ano de nascimento: '))
		
		# calcula-se a idade do usuário no ano em vigor
		idade = ano_atual - ano
		
		# se a idade for maior ou igual a 21 anos, ele vai para o grupo das pessoas que possuem a mesma caracteristica.
		if idade >= 21:
			x = x + 1
		# caso contrário, ele vai para o grupo das pessoas que possuem idade menor que 21 anos.
		else:
			y = y + 1
	
	# exibe-se o resultado da pesquisa.
	linha()
	print('RESULTADO'.center(60))
	linha()
	print(f'\t{x} pessoas têm idade igual ou superior a 21 anos.\n\t{y} pessoas têm idade inferior a 21 anos.'.center(60))
	linha()


if __name__ == '__main__':
	main()

