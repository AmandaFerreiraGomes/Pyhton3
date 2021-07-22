""" Desafio 084: """
# Programa Principal:


def main():
	cond = 'S'
	data = []
	todos = []
	x = y = 0
	while True:
		if cond == 'N':
			print('Coleta Finalizada!')
			break
		elif cond == 'S':
			nome = str(input('Nome: '))
			peso = float(input('Peso(kg): '))
			data.append(nome)
			data.append(peso)
			todos.append(data[:])
			data.clear()
		else:
			print('Condição Inválida.')
			cond = str(input('Deseja Continuar[S/N]? ')).upper()
		cond = str(input('Deseja Continuar[S/N]? ')).upper()
	
	if len(todos) == 0:
		print('Não há cadastrados!')
	if len(todos) == 1:
		print(f'{len(todos)} pessoa foi cadastrada.')
	else:
		print(f'{len(todos)} pessoas foram cadastradas.')
	leves = []
	pesadas = []
	media = []
	z = 0
	for p in todos:
		if p[1] >= 100.0:
			x = x + 1
			pesadas.append(p[0])
		elif p[1] <= 70.0:
			y = y + 1
			leves.append(p[0])
		else:
			z = z + 1
			media.append(p[0])
	print(f'{x} pessoas acima de 100 kg: {pesadas}')
	print(f'{y} pessoas abaixo de 70 kg: {leves}')
	print(f'{z} pessoas entre 70kg e 100kg: {media}')


main()
