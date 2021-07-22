""" Desafio 062: """
# Programa Principal:


def main():
	a1 = int(input('Digite o primeiro termo(a1): '))
	r = int(input('Digite a razão(r): '))
	c = 0
	an = a1
	mostrar = 9
	print(f'{a1}', end='')
	while c <= mostrar:
		if c == mostrar:
			mostrar = int(input('\nDigite quantos termos você deseja mostrar: '))
			c = 0
			if mostrar == 0:
				break
		an = an + r
		print(f' {an}', end='')
		c = c + 1
	print('PROGRAMA FINALIZADO COM SUCESSO!')
		
	
main()
