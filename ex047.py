""" Desafio 047: """
# Programa Principal:


def main():
	print('\033[34mNúmeros Pares entre 1 e 50: \033[m')
	for e in range(1, 50):
		if e % 2 == 0:
			par = e
			print('->', par)
		
		
main()
