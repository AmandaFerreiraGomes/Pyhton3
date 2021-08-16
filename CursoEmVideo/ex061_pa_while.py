""" Desafio 061: """


def linha():
	print('-' * 60)


# Programa Principal:
def main():
	
	# entrada de valores:
	linha()
	a1 = int(input('Digite o primeiro termo(a1): '))
	r = int(input('Digite a razão(r): '))
	linha()

	#cabeçalho:
	print(f'10 primeiros termos da P.A. de razão = {r} e a1 = {a1}.'.center(60))
	linha()
	
	c = 0
	an = a1
	
	# imprime o primeiro elemento da progressão aritmética:
	print(f'{a1},', end='')
	
	# enquanto c for menor que nove
	while c < 9:
		# an é o último elemento, mas também é o próximo elemento quando somado à razão r.
		an = an + r
		
		# aqui trata sobre forma de imprimir na tela, se c for 8, significa que é o último termo da P.A., portanto
		# não tem vígula antes nem depois.
		if c == 8:
			print(f' {an}')
		# caso contrário, imprime-se an com a vírgula depois
		else:
			print(f' {an},', end='')
			
		# incrementa-se c em 1 unidade.
		c = c + 1
	
	linha()
	print('PROGRAMA FINALIZADO COM SUCESSO!'.center(60))
	linha()
	
	
if __name__ == '__main__':
	main()
