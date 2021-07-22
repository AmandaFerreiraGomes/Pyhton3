""" Desafio 065: """
# Programa Principal:


def main():
	num = 0
	s = 0
	x = 0
	cond = ''
	n = []
	while cond != 'N':
		num = int(input('Digite um número: '))
		cond = str(input('Deseja continuar[S/N]?')).strip().upper()
		n.append(num)
		if cond == 'N':
			cond = False
			break
		s = s + num
		x = x + 1
	maior = max(n)
	menor = min(n)
	print(f'Média: {s/x:.2f}')
	print(f'Maior: {maior} e Menor: {menor}')
	
	
main()
