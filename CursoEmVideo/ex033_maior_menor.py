""" Desafio 033: """

# função que cria um dicionário de cores, porém só foi inserida a cor azul, e retorna a cor azul.
def azul():
	cores = {
		'azul': '\033[34m'
	}
	return cores['azul']


def linha():
	print(f'{azul()}-'*30)

# Programa Principal:

if __name__ == "__main__":
	linha()
	# solicita que o usuário digite três números
	a = int(input('Digite um número: '))
	b = int(input('Digite outro: '))
	c = int(input('Digite o último: '))
	linha()
	
	# atribui às variáveis maior e menor os valores de a e b, respectivamente.
	menor = a
	maior = b
	# com essas atribuições, a começa sendo o menor valor e b começa sendo o maior valor
	# se não houver números maiores que b, então ele continua sendo o maior, caso contrário, a variável maior é reatribuída a outro valor.
	# o mesmo ocorre com a variável menor.
	
	# verifica se a é maior que b e que c
	if b < a and c < a:
		maior = a # se for, maior = a
	if b < c and a < c: # verifica se c é maior que a e b
		maior = c # se for, maior = c
	if b < a  and b < c: # verifica se b é menor que a e c
		menor = b # se for, menor = b
	if c < a and c < b: # se c é menor que a e b, então c é o menor valor
		menor = c # se for, menor = c
	
	# exibe os valores maior e menor
	print(f'Maior: {maior}\nMenor: {menor}')
	linha()
