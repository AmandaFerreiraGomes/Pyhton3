""" Desafio 043: """
# Programa Principal:


def main():
	peso = float(input('Digite seu peso (em kg): '))
	altura = float(input('Digite sua altura (em m): '))
	imc = (peso/(altura**2))
	print('----------STATUS----------')
	if imc < 18.5:
		print(f'IMC: {imc:.2f}\nAbaixo do Peso.')
	elif 18.5 < imc < 25.0:
		print(f'IMC: {imc:.2f}\nPeso Ideal.')
	elif 25.0 < imc < 30.0:
		print(f'IMC: {imc:.2f}\nSobrepeso.')
	elif 30.0 < imc < 40.0:
		print(f'IMC: {imc:.2f}\nObesidade.')
	else:
		print(f'IMC: {imc:.2f}\nObesidade Mórbida.')
	
main()
