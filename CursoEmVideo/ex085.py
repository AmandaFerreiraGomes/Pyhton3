""" Desafio 085: """
# Programa Principal:


def main():
	par = []
	impar = []
	numeros = []
	y = x = 0
	for n in range(0, 7):
		num = int(input('Digite um número: '))
		if num % 2 == 0:
			par.append(num)
			par.sort()
		else:
			x = x + 1
			impar.append(num)
			impar.sort()
	
	numeros.append(par[:])
	numeros.append(impar[:])
	print(f'Pares: {numeros[0]}')
	print(f'Ímpares: {numeros[1]}')


main()
