""" Desafio 071: """
# Programa Principal:


"""def main():
	valor = float(input('Digite o valor a ser sacado: R$ '))
	cedulas = 0
	atual = 100.0
	while True:
		if atual <= valor:
			valor = valor - atual
			cedulas += 1
		else:
			print(f'{cedulas} cédulas de R$ {atual:.2f}')
			if valor == 0:
				break
			if atual == 100.0:
				atual = 50
			elif atual == 50.0:
				atual = 20.0
			elif atual == 20.0:
				atual = 10.0
			elif atual == 10:
				atual = 5.0
			elif atual == 5.0:
				atual = 2.0
			elif atual == 2.0:
				atual = 1.0
			cedulas = 0
	print('FINALIZADO!')
	
	
main()"""


def main():
	welcome = 'BEM-VINDO(A) AO BANCO AFG'
	print(f'{welcome:=^35}')
	dolar = float(input('Quanto você deseja converter? US$ '))
	cot_day = float(input('Cotação do Dólar no dia: R$ '))
	conv = dolar * cot_day
	print(f'Total: R$ {conv:.2f}')
	print(f'='*35)
	valor = conv
	ced = 0
	cent = 0.50
	aux = valor
	inicio = 50.0
	while True:
		if inicio <= aux:
			aux = aux - inicio
			ced = ced + 1
		else:
			print(f'{ced} cédulas de R${inicio}')
			if inicio == 50.0:
				inicio = 20.0
			elif inicio == 20.0:
				inicio = 10.0
			elif inicio == 10.0:
				inicio = 1.0
			ced = 0
			if aux == 0:
				print('===========FINALIZADO===========')
				break


main()
