""" Desafio 063: """
# Programa Principal:


def main():
	n = int(input('Digite um número: '))
	prox = ant = 1
	x = 0
	y = 'SEQUÊNCIA DE FIBONACCI: '
	z = len(y)
	j = z//2
	print('-='*j)
	print(y)
	print('-='*j)
	while x < n:
		aux = ant
		if ant == 1 and ant == prox:
			prox = 1
		if x != (n-1):
			print(f' {aux}->', end='')
		else:
			print(f' {aux}', end='')
		ant = prox
		prox = prox + aux
		x = x + 1
	print('\nPROGRAMA FINALIZADO COM SUCESSO!')
	
main()
