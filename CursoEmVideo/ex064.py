""" Desafio 064: """
# Programa Principal:


def main():
	num = 0
	x = 0
	s = 0
	while num != 999:
		num = int(input('Digite um número(999 para sair): '))
		x = x + 1
		if num != 999:
			s = s + num
	print(f'Foram digitados {x} números e a soma entre eles é {s}')

	
main()
