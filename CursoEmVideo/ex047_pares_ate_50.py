def linha():
	print('-' * 69)


def main():
	
	linha()
	print('\033[34m', end='')
	print(f'------------------- Números Pares entre 1 e 50: ---------------------'.upper())
	print('\033[m', end='')
	linha()
	
	for e in range(1, 50):
		if e % 2 == 0:
			print(f'\033[36m{e} ', end='')
	
	print('\033[m\n', end='')
	linha()


if __name__ == "__main__":
	main()
