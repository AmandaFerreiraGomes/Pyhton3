""" Desafio 032: """


def linha():
	print('-'*31)


# Programa Principal:
if __name__ == "__main__":
	
	linha()
	print("          É BISSEXTO?          ")
	linha()
	
	# solicito que o usuário digite um ano
	ano = int(input('Digite o ano: '))
	linha()
	
	# se o resto da divisão de ano por 4 for zero E ( o resto da divisão de ano por 400 for zero OU o resto da divisão de ano por 100 for diferente de zero)
	# o ano é bissexto, caso contrário o ano não é bissexto.
	if ano % 4 == 0 and (ano % 400 == 0 or ano % 100 != 0):
		print(f'{ano} é BISSEXTO!')
	else:
		print(f'{ano} não é BISSEXTO!')
