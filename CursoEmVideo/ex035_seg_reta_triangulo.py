""" Desafio 035: """


def linha():
	print('-' * 45)


# Programa Principal:
if __name__ == "__main__":
	
	# solicita que o usuário entre com três medidas de segmento de reta
	linha()
	a = float(input('Digite o tamanho do segmento de reta(em cm): '))
	b = float(input('Digite o tamanho do segmento de reta(em cm): '))
	c = float(input('Digite o tamanho do segmento de reta(em cm): '))
	linha()
	
	# verifica se os segmentos a, b e c podem formar um triângulo.
	"""
	Condição de existência de um triângulo

	Para construir um triângulo não podemos utilizar qualquer medida, tem que seguir a condição de existência:
	Para construir um triângulo é necessário que a medida de qualquer um dos lados seja menor que a soma das medidas dos outros dois e maior que o valor absoluto da diferença entre essas medidas.



	| b - c | < a < b + c
	| a - c | < b < a + c
	| a - b | < c < a + b
	
	Fonte: https://brasilescola.uol.com.br/matematica/triangulo.htm#:~:text=Tri%C3%A2ngulo%20%C3%A9%20uma%20figura%20geom%C3%A9trica,%C3%A2ngulos%20internos%20%C3%A9%20sempre%20180%C2%BA.
	"""
	
	if (abs(b-c) < a < c + b) and (abs(a-c) < b < a + c) and (abs(a-b) < c < a + b):
		print('Sim, eles podem formar um TRIANGULO!')
	else:
		print('Não, eles não podem formar um TRIANGULO!')
