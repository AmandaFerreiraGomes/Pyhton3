""" Desafio 039: """
# Programa Principal:


def linha():
	print('-' * 35)


if __name__ == "__main__":
	
	# cabeçalho:
	linha()
	print('----- SITUAÇÃO DE ALISTAMENTO -----')
	
	# entrada de dados
	linha()
	ano = int(input('Digite seu ano de nascimento: '))
	ano_atual = int(input('Digite o ano em que estamos: '))
	linha()
	
	# cálculo da atual idade do usuário
	idade = ano_atual - ano
	
	# se a idade for maior que 18 anos, então o usuário recebe uma mensagem de que deveria ter se alistado há mais tempo
	if idade > 18:
		print(f'\033[34mCom {idade} anos, você perdeu o prazo para se alistar! Há {idade-18} anos seria o ideal.')
	# se a idade for menor que 18 anos, o usuário recebe a mensagem que mostra quanto tempo ainda falta para ele se alistar
	elif idade < 18:
		print(f'\033[34mCom {idade} anos, você ainda vai se alistar! Faltam {18-idade} anos.')
	# em último caso, significa que o usuário tem 18 anos, portanto está na hora de se alistar
	else:
		print(f'\033[34mCom {idade} anos, está na hora de você se alistar!')
	
