""" Desafio 040: """
# Programa Principal:


def main():
	nota1 = float(input('Nota 1: '))
	nota2 = float(input('Nota 2: '))
	med = (nota1 + nota2)/2
	if med < 5.0:
		print(f'\033[30:44mMédia: {med}. REPROVADO!\033[m')
	elif 5.0 < med < 6.9:
		print(f'\033[30:44mMédia: {med}. RECUPERAÇÃO!\033[m')
	else:
		print(f'\033[30:44mMédia: {med}. APROVADO!\033[m')
	
	
main()
