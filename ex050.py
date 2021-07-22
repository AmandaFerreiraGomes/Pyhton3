""" Desafio 050: """
# Programa Principal:


def main():
	s = 0
	print('--------Soma dos Pares--------')
	for e in range(0, 6):
		n = int(input(f'Digite o {e+1} número: '))
		if n % 2 == 0:
			s = s + n
	print(f'Soma: {s}')

	
main()
