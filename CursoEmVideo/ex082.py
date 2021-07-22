""" Desafio 082: """
# Programa Principal:


def main():
	"""cond = 'S'
	par = []
	impar = []
	lista = []
	while True:
		if cond in 'Nn':
			print(par)
			print(impar)
			print(par + impar)
			break
		elif cond in 'Ss':
			num = int(input('Digite um número: '))
			if num % 2 == 0:
				par.append(num)
			else:
				impar.append(num)
		else:
			print('Condição Inválida!')
			cond = str(input('Você deseja continuar[S/N]?'))
		cond = str(input('Você deseja continuar[S/N]?'))

"""
	cond = 'S'
	par = []
	impar = []
	lista = []
	while True:
		print('=' * 30)
		if cond in 'Nn':
			break
		elif cond in 'Ss':
			num = int(input('Digite um  número: '))
			lista.append(num)
		else:
			print('=' * 30)
			print('Condição Inválida!')
			cond = str(input('Deseja continuar [S/N]? '))
		cond = str(input('Deseja continuar [S/N]? '))
	print('RESULTADOS')
	print('='*30)
	print(f'Lista Inserida: {lista}')
	print('=' * 30)
	for e in lista:
		if e % 2 == 0:
			par.append(e)
		else:
			impar.append(e)
	par.sort()
	impar.sort()
	print(f'Números Ímpares: {impar}')
	print('=' * 30)
	print(f'Números Pares: {par}')
	print('=' * 30)
	

main()
