""" Desafio 052: """


# Programa Principal:


def main():
	print('---------------------------')
	for e in range(1, 100):
		n = e
		primo = False
		if n > 1 and (not (n > 2 and n % 2 == 0)) and (not (n > 3 and n % 3 == 0)) and (not (n > 5 and n % 5 == 0)) and (
				not (n > 7 and n % 7 == 0)):
			primo = True
		if primo:
			print(f'{n} é primo!')
		else:
			print(f'{n} não é primo!')


main()

"""Números maiores que 1, não divisíveis por 2, além do próprio 2 """
