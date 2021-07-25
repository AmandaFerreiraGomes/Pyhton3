""" Desafio 040: """


def linha():
	print('-' * 23)


# Programa Principal:
if __name__ == "__main__":
	
	#cabeçalho:
	linha()
	print("----- MÉDIA FINAL -----")
	linha()
	
	# pede que o usuário insira as notas sobre as quais será calculada a média.
	nota1 = float(input('Nota 1: '))
	nota2 = float(input('Nota 2: '))
	
	# como são duas notas, divide-se por dois
	med = (nota1 + nota2)/2
	
	linha()
	# se a média calculada for menor que 5, o aluno estará reprovado
	if med < 5.0:
		print(f'\033[31mMédia: {med}. REPROVADO!\033[m')
	# caso a média esteja entre 5 e 6.9, o aluno ficará de recuperação
	elif 5.0 < med < 7.0:
		print(f'\033[36mMédia: {med}. RECUPERAÇÃO!\033[m')
	# por fim, a última situação é a de aprovado, em que o aluno possui média maior ou igual a 7.0
	else:
		print(f'\033[34mMédia: {med}. APROVADO!\033[m')
	linha()
