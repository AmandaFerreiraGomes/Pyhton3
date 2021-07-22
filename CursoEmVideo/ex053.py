""" Desafio 053: """
# Programa Principal:

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = frase.replace(' ', '')
inverso = junto[::-1]
# for letra in range(len(junto)-1, -1, -1):
#	inverso = inverso + junto[letra]
print(f'Frase: {frase}')
print(f'Inverso: {inverso}')
if inverso == junto:
	print('A frase digitada é um palíndromo!')
else:
	print('A frase digitada não é um palíndromo!')
