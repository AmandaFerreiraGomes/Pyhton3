def nro_primo():
	print('---------------------------')
	for n in range(1, 101):

		primo = False
		if n > 1 and (not (n > 2 and n % 2 == 0)) and (not (n > 3 and n % 3 == 0)) and (not (n > 5 and n % 5 == 0)) and (
				not (n > 7 and n % 7 == 0)):
			primo = True
		if primo:
			print(f'{n} é primo!')
		else:
			print(f'{n} não é primo!')


if __name__ == "__main__":
	nro_primo()