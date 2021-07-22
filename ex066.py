""" Desafio 066: """
# Programa Principal:


def main():
	n = c = s = 0
	while n != 7777:
		n = int(input('Digite um número (7777 para parar): '))
		if n == 7777:
			break
		else:
			c = c + 1
			s = s + n
	print(f'Foram digitados {c} valores e a soma entre eles foi {s}')


main()
