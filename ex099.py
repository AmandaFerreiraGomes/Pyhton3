""" Desafio 099: """
# Funções Personalizadas:


def maior(num):
	lista = []
	for e in num:
		lista.append(e)
	maximo = max(lista)
	print(f'Maior valor recebido: {maximo}')


# Programa Principal:


def main():
	cond = 'S'
	lista = []
	while True:
		if cond == 'N':
			break
		elif cond == 'S':
			numero = int(input('Digite um número: '))
			lista.append(numero)
			cond = str(input('Deseja Continuar[S/N]?')).upper()[0]
		else:
			print('Condição Inválida!')
			cond = str(input('Deseja Continuar[S/N]?')).upper()[0]
	print(f'Foram passados {len(lista)} valores.')
	maior(lista)
	
	print('Fim!')


main()
