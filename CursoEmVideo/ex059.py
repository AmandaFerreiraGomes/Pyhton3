""" Desafio 059: """
# Programa Principal:


def main():
	print('-='*25)
	a = float(input('Digite um número: '))
	b = float(input('Digite outro: '))
	print('-=' * 25)
	c = 0
	while c != 5:
		c = int(input("""\033[36m\t\t-> MENU DE OPERAÇÕES: \033[m
		\033[36m[1]\033[m - \033[30mSOMAR.\033[m
		\033[36m[2]\033[m - \033[30mMULTIPLICAR.\033[m
		\033[36m[3]\033[m - \033[30mMAIOR.\033[m
		\033[36m[4]\033[m - \033[30mNOVOS VALORES.\033[m
		\033[36m[5]\033[m - \033[30mSAIR DO PROGRAMA.\033[m\n"""))
		if c == 1:
			soma = a + b
			print(f'\033[34mSoma: {soma}.\033[m')
		elif c == 2:
			multip = a * b
			print(f'\033[34mMultiplicação: {multip}.\033[m')
		elif c == 3:
			maior = a
			if b > a:
				maior = b
			else:
				maior = a
			print(f'\033[34mMaior: {maior}.\033[m')
		elif c == 4:
			e = float(input('Digite um valor: '))
			f = float(input('Digite outro: '))
			a = e
			b = f
			print(f'\033[34mOs novos valores digitados foram: {a} e {b}.\033[m')
		print('-=' * 25)
	print('\033[36mPROGRAMA EXECUTADO COM SUCESSO!\033[m')
	print('-=' * 25)

	
main()
