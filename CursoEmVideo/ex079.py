""" Desafio 079: """
# Programa Principal:


def main():
	x = 0
	cond = 'S'
	num = []
	while True:
		if cond == 'N':
			num.sort()
			print(num)
			break
		elif cond == 'S':
			n = int(input('Digite um número: '))
			if n in num:
				print('Valor já inserido!')
				n = int(input('Digite um número: '))
			else:
				num.append(n)
		else:
			print('Condição Inválida')
		cond = str(input('Deseja continuar[S/N]?')).upper()
		
		



main()
