""" Desafio 038: """


def linha():
	print('-' * 31)


# Programa Principal:


if __name__ == "__main__":
	
	#cabeçalho:
	linha()
	print('-------- SÃO IGUAIS? ----------')
	linha()
	
	# o usuário digita dois números, os quais serão analisados posteriormente.
	a = int(input('Digite um número: '))
	b = int(input('Digite outro: '))
	
	# é atribuído à variável maior o valor digitado para a
	maior = a
	
	# se a for igual a b, então não existe um valor maior, já que ambos são iguais
	if a == b:
		print('Não existe valor maior, os dois são iguais!')
	# se b for maior que a, então é exibida a mensagem
	elif b > a:
		print('O segundo valor é maior!')
	# por fim, caso nenhuma das condições anteriores seja válida, o primeiro valor é o maior e é exibida a mensagem
	else:
		print(f'O primeiro valor é o maior!')
		
