""" Desafio 060: """


from math import factorial


def linha():
	print('-' * 30)

	
# Programa Principal:
def main():
	
	print('\033[36m-=\033[m'*25)
	
	f = int(input('Digite um número: '))
	
	c = f
	
	fat = factorial(f)
	
	print(f'-=-=-=-=-=-= FATORIAL DE {f}! -=-=-=-=-=-=')
	
	while c >= 1:
		if c == 1:
			print(f' {c} = {fat}')
		else:
			print(f' {c} x', end='')
		c = c - 1
		
	
if __name__ == '__main__':
	main()
