""" Desafio 039: """
# Programa Principal:


def main():
	ano = int(input('Digite seu ano de nascimento: '))
	ano_atual = int(input('Digite o ano em que estamos: '))
	idade = ano_atual - ano
	if idade > 18:
		print(f'\033[34mCom {idade} anos, você perdeu o prazo para se alistar! Há {idade-18} anos seria o ideal.')
	elif idade < 18:
		print(f'\033[34mCom {idade} anos, você ainda vai se alistar! Faltam {18-idade} anos.')
	else:
		print(f'\033[34mCom {idade} anos, está na hora de você se alistar!')
		
	
main()
