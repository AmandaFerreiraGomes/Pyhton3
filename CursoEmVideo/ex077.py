""" Desafio 077: """
# Programa Principal:


def main():
	pal = ('abacate', 'leite', 'farinha', 'tomate')
	palavras = list(pal)
	x = y = 0
	while y < len(palavras[y]):
		a = e = i = o = u = 0
		c = 'a e i o u'
		print(f'{palavras[y].upper():=^48}')
		if 'a' or 'e' or 'i' or 'o' or 'u' in palavras[y]:
			a = palavras[y].count('a')
			e = palavras[y].count('e')
			i = palavras[y].count('i')
			o = palavras[y].count('o')
			u = palavras[y].count('u')
		print(f'Vogais: A -> {a}, E -> {e}, I -> {i}, O -> {o}, U -> {u}')
		y = y + 1
		if y == len(palavras):
			break
	print('='*48)
	
	
main()
