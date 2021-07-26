""" Desafio 043: """


def linha():
	print('-' * 41)
	
	
# Programa Principal:
if __name__ == "__main__":
	
	# cabeçalho
	linha()
	print('-- CÁLCULO DO ÍNDICE DE MASSA CORPORAL --')
	linha()
	
	# entrada de dados
	peso = float(input('Digite seu peso (em kg): '))
	altura = float(input('Digite sua altura (em m): '))
	
	# cálculo do imc: peso dividido pela altura ao quadrado
	imc = (peso/(altura**2))
	
	# status do imc do usuário
	linha()
	print('----------------- STATUS ----------------')
	linha()
	# se o imc for menor que 18.5, que é o ideal, exibe-se que o usuário está abaixo do peso
	if imc < 18.5:
		a = 'Abaixo do Peso.'
	# se o imc está entre 18.5 e  25.0, então o usuário verá que está com o peso ideal
	elif 18.5 < imc < 25.0:
		a = 'Peso Ideal.'
	# se o imc estiver entre 25.0 e 30.0, então o usuário está com sobrepeso
	elif 25.0 < imc < 30.0:
		a = 'Sobrepeso.'
	# se o imc estiver entre 30 e 40, então o usuário está com obesidade mórbida
	elif 30.0 < imc < 40.0:
		a = 'Obesidade.'
	# por fim, se o usuário tiver imc acima de 40.0, então ele estará com obesidade mórbida
	else:
		a = 'Obesidade Mórbida.'
	
	# exibe-se o resultado
	print(f'IMC: {imc:.2f}\n{a}')
	
