""" Desafio 062: """


def linha():
	print('-' * 60)


# Programa Principal:
def main():
	
	linha()
	print('PROGRESSAO ARITMETICA'.center(60))
	linha()
	a1 = int(input('Digite o primeiro termo(a1): '))
	r = int(input('Digite a razão(r): '))
	linha()
	
	c = 0
	an = a1
	mostrar = 9
	
	print(f'{a1}', end='')
	
	# COMO c COMEÇA COM ZERO, ENTÃO MOSTRAR VAI ATÉ 9, PARA QUE HAJAM DEZ ELEMENTOS.
	while c <= mostrar:
		if c == mostrar:
			print()
			linha()
			mostrar = int(input('\nDigite quantos termos você deseja mostrar (0 para sair): '))
			c = 0
			if mostrar == 0:
				break
		an = an + r
		print(f' {an}', end='')
		c = c + 1
		
	linha()
	print('PROGRAMA FINALIZADO COM SUCESSO!'.center(60))
	linha()


if __name__ == '__main__':
	main()
