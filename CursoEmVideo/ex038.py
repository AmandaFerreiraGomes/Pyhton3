""" Desafio 038: """
# Programa Principal:


def main():
	a = int(input('Digite um número: '))
	b = int(input('Digite outro: '))
	maior = a
	if a == b:
		print('Não existe valor maior, os dois são iguais!')
	elif b > a:
		print('O segundo valor é maior!')
	else:
		print(f'O primeiro valor é o maior!')
		

main()
