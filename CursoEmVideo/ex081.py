""" Desafio 080: """
# Programa Principal:


def main():
	lista = []
	x = z = 0
	cond = 'S'
	while True:
		cond = str(input('Você deseja continuar[S/N]?'))
		if cond in 'Ss':
			n = int(input('Digite um número: '))
			if n in lista:
				print('O valor já está na lista.')
				z = z + 1
			else:
				lista.append(n)
				x = x + 1
		elif cond in 'Nn':
			print(f'Foram digitados {x+z} números')
			lista.sort(reverse=True)
			print(lista)
			break
		else:
			print('Condição Inválida!')
			cond = str(input('Você deseja continuar[S/N]?'))


main()
