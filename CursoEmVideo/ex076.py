""" Desafio 076: """
# Programa Principal:


def main():
	prod_precos = ('', 'Arroz', 'Biscoito', 'Leite', 'Macarrão', 'Sorvete', 'Chá', 3.5, 5.0, 12.0, 3.0, 6.5, 1.5)
	x = (len(prod_precos)//2)
	m = 'TABELA DE PREÇOS'
	print('='*27)
	print(f'{m:^27}')
	print('=' * 27)
	cif = 'R$'
	for e in range(1, x):
		n = prod_precos[e]
		p = prod_precos[(e+x)]
		print(f'{n:.<12}{cif:.>8}{p:6.2f}')
	

main()
