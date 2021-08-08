""" Desafio 051: """


def linha():
	print('-'*53)


# Programa Principal:
def main():
	
	# inicializa-se a variável x com 1, pois a contagem começa com a1.
	x = 1
	
	linha()
	# solicita-se que o usuário entre com o termo a1 e com a razão r.
	a1 = int(input('Digite o primeiro termo da P.A.: '))
	r = int(input('Digite a razão da P.A.: '))
	
	# cabecalho.
	linha()
	print('--------- Dez primeiros termos da sequência ---------')
	linha()
	
	# para e no intervalo que condiz com o início no primeiro elemento até o último elemento, que é a10 com razão dois.
	# na p.a. o enésimo termo é calculado an = a1 + n*r, em que an é o enésimo termo e n é a posição do enésimo termo
	# a1 é o primeiro termo da p.a. e r é a razão.
	for e in range(a1, (a1 + 10*r), r):
		print(f'a{x} = {e}')
		x = x + 1 # a cada loop, acrescenta-se uma unidade ao contador x.
	
	linha()
	

if __name__ == '__main__':
	main()

