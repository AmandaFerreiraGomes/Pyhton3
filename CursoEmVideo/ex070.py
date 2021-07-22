""" Desafio 070: """
# Programa Principal:


def main():
	s = 0.0
	cond = 1
	x = y = 0
	barato = ' '
	caro = ' '
	menor = maior = 0
	while True:
		print('\033[34m==\033[m'*25)
		nome_prod = str(input('Digite o nome do produto: '))
		preco = float(input('Digite o preço do produto: R$ '))
		s = s + preco
		if preco > 1000.0:
			x = x + 1
		y = y + 1
		if y == 1:
			menor = preco
			maior = preco
			barato = nome_prod
			caro = nome_prod
		else:
			if preco < menor:
				menor = preco
				barato = nome_prod
			if preco > maior:
				maior = preco
				caro = nome_prod
		print('-=' * 25)
		cond = str(input('\033[31mDigite 0 para sair 1 para continuar: \033[m'))
		print('-=' * 25)
		if cond == '0':
			sx = 'Compra Finalizada!'
			print(f'{sx:-^40}')
			break
	print(f'Total R$ {s:.2f}')
	print(f'{x} produtos custam mais de R$ 1.000,00.')
	print(f'O produto mais barato é {barato} e custa R$ {menor:.2f}')
	print(f'O produto mais caro é {caro} e custa R$ {maior:.2f}')


main()
