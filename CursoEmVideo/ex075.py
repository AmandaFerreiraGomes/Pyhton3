""" Desafio 075: """
# Programa Principal:


def main():
	lst = []
	par = []
	for e in range(0, 4):
		num = int(input('Digite um número: '))
		if num % 2 == 0:
			par.append(num)
		lst.append(num)
	t = tuple(lst)
	p = tuple(par)
	print(f'Repetições do valor 9: {t.count(9)}')
	print(f'Posição do valor: {t.index(3)+1}')
	print(f'Pares: {p}.')
	del(p, t)


main()
