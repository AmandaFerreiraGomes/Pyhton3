""" Desafio 072: """


# Programa Principal:


def main():
	num = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
	num_ext = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze'
			, 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
	print('=' * 30)
	numero_user = 0
	numero_user = int(input('Digite um número (entre 0 a 20): '))
	while True:
		print('=' * 30)
		if 20 > numero_user > 0:
			p = num.index(numero_user)
			print(f'{numero_user} = {num_ext[p]}')
			break
		if numero_user > 20 or numero_user < 0:
			print(f'Valor Inválido!')
			numero_user = int(input('Digite um número (entre 0 e 20): '))
		
		
	


main()
