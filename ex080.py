""" Desafio 080: """
# Programa Principal:


def main():
	""" Resolução do Guanabara
	lista = list()
	for n in range(0, 5):
		num = int(input('Digite um número: '))
		if n == 0 or num > lista[len(lista)-1]:
			lista.insert(n, num)
		else:
			x = 0
			while x < len(lista):
				if num <= lista[x]:
					lista.insert(x, num)
					break
				x = x + 1
	print(f'Os valores digitados em ordem foram: {lista}')"""
	
	lista = []
	for e in range(0, 5):
		num = int(input('Digite um número: '))
		if e == 0:
			lista.append(num)
		elif num > lista[len(lista)-1]:
			lista.insert(e, num)
		else:
			i = 0
			while i < len(lista):
				if num <= lista[i]:
					lista.insert(i, num)
					break
				i = i + 1
	print(lista)


main()
