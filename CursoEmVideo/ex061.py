""" Desafio 061: """
# Programa Principal:


def main():
	a1 = int(input('Digite o primeiro termo(a1): '))
	r = int(input('Digite a razão(r): '))
	c = 0
	an = a1
	print(f'{a1},', end='')
	while c < 9:
		an = an + r
		if c == 8:
			print(f' {an}')
		else:
			print(f' {an},', end='')
		c = c + 1
	print('PROGRAMA FINALIZADO COM SUCESSO!')
	
	
main()
