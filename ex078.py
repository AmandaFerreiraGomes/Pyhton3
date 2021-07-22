""" Desafio 078: """
# Programa Principal:


def main():
	valores = list()
	for e in range(0, 5):
		valores.append(int(input(f'Digite um número na posição {e+1}: ')))
	menor = min(valores)
	maior = max(valores)
	print(f'Menor: {menor} na posição {valores.index(menor)+1}')
	print(f'Maior: {maior} na posição {valores.index(maior)+1}')
	
	
main()
