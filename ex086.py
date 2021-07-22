""" Desafio 086: """
# Programa Principal:


def main():
	i = 0
	j = 0
	m = [i][j]
	lista1 = []
	lista2 = []
	lista3 = []
	for i in range(0, 3):
		for j in range(0, 3):
			num = int(input(f'Digite um número para a posição [{i}]{[j]}: '))
			if i == 0:
				lista1.append(num)
			elif i == 1:
				lista2.append(num)
			elif i == 2:
				lista3.append(num)
	x = 0
	for p in range(0, 3):
		print(f' [{lista1[p]}] ', end='')
	print()
	for e in range(0, 3):
		print(f' [{lista2[e]}] ', end='')
	print()
	for f in range(0, 3):
		print(f' [{lista3[f]}] ', end='')
			


main()
