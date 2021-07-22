""" Desafio 098: """
from time import sleep
# Funções Personalizadas:


def contador(a1, an, r):
	"""
	:param a1: parâmetro inicial.
	:param an: parâmetro final.
	:param r: razão da contagem.
	:return: não há retorno.
	"""
	lista = []
	if r == 0:
		r = 1
	if an < a1:
		r = (-1)*r

	if r > 0:
		while a1 <= an:
			print(f'{a1}', end=' ')
			a1 = a1 + r
	else:
		while an <= a1:
			lista.append(an)
			an = an - r
		lista.sort(reverse=True)
		for e in lista:
			print(e, end=' ')


# Programa Principal:


def main():
	print('-=' * 16)
	print('Contagem de 10 até 0, de 2 em 2:')
	contador(10, 0, 2)
	print('\n')
	print('-=' * 16)
	print(f'Contagem de 1 até 10, de 1 em 1:')
	contador(1, 10, 1)
	print('\n')
	print('-='*16)
	print('   PERSONALIZE A CONTAGEM:  ')
	print('-=' * 16)
	a1 = int(input('\na1 = '))
	an = int(input('an = '))
	r = int(input('r = '))
	print('-='*16)
	print(f'Contagem de {a1} até {an}, de {r} em {r}.')
	contador(a1, an, r)


main()
