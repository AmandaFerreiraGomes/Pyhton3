""" Desafio 083: """
# Programa Principal:


def main():
	exp = str(input('Digite uma expressão entre parênteses: '))
	ex = list()
	for e in exp:
		if e == '(':
			ex.append('(')
		elif e == ')':
			if len(ex)>0:
				ex.remove('(')
			else:
				ex.append(')')
				break

	if len(ex) == 0:
		print('Expressão Correta!')
	else:
		print('Expressão Incorreta!')


main()
