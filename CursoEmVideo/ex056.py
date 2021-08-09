""" Desafio 056: """


def linha():
	print('-' * 55)


# Programa Principal:
def main():
	
	# cabeçalho do programa.
	linha()
	print(f' PESQUISA DE PÚBLICO '.center(55))
	linha()
	
	s = 0
	maioridade = 0
	nomevelho = ''
	x = 0
	
	for e in range(0, 2):
		
		# cabeçalho da pesquisa.
		linha()
		print(f' PESSOA: {e+1} '.center(55, ' '))
		linha()
		
		nome = str(input('Digite seu nome: ')).strip()
		idade = int(input(f'Olá, {nome}! Quantos anos você tem? '))
		linha()
		sexo = str(input('Sexo: \nF - FEMININO\nM - MASCULINO\n: ')).strip().upper()
		
		# soma das idades inseridas pelo usuario.
		s = s + idade
		
		# caso seja o segundo loop e sexo for igual a M...
		if e == 1 and sexo == 'M':
			nomevelho = nome
			maioridade = idade
		
		# se sexo for M e idade for maior que a maioridade ja definida, nomevelho, que é a variável para o
		# nome do homem mais velho recebe o nome do atual homem mais velho
		if sexo == 'M' and idade > maioridade:
			nomevelho = nome
			maioridade = idade
		
		# se sexo for F e a idade dessa mulher for maior que 20 anos, então ela entra para a
		# contagem de mulheres com essa característica.
		if sexo == 'F' and idade > 20:
			x = x + 1

	# calcula-se a média da soma das idades.
	med = (s/2)
	
	linha()
	
	# exibe-se o resultado da média das idades das pessoas que fazem parte do grupo.
	print(f'1. Média de Idade do Grupo: {med}.')
	
	# exibe-se a idade do homem mais velho do grupo.
	print(f'2. O homem mais velho tem {maioridade} ano(s) e seu nome é {nomevelho}.')
	
	# exibe-se a quantidade de mulheres que têm mais de 20 anos.
	print(f'3. {x} mulher(es) tem(êm) mais de 20 anos.')
	
	linha()
	

if __name__ == '__main__':
	main()
