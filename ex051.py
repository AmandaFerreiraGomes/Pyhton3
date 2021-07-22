""" Desafio 051: """
# Programa Principal:


def main():
	x = 1
	print('-----------------------------------------------------')
	a1 = int(input('Digite o primeiro termo da P.A.: '))
	r = int(input('Digite a razão da P.A.: '))
	print('--------- Dez primeiros termos da sequência ---------')
	for e in range(a1, a1+11, r):
		print(f'a{x} = {e}')
		x = x + 1
	
	
main()
