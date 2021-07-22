""" Desafio 056: """
# Programa Principal:


def main():
	s = 0
	med = 0
	maioridade = 0
	nomevelho = ''
	m20 = 0
	x = 0
	for e in range(0, 5):
		print(f'---------------PESSOA: {e+1}---------------')
		nome = str(input('Digite seu nome: ')).strip()
		idade = int(input(f'Olá, {nome}! Quantos anos você tem? '))
		sexo = str(input('Sexo: -\nF - FEMININO\nM - MASCULINO: ')).strip().upper()
		s = s + idade
		if e == 1 and sexo == 'M':
			nomevelho = nome
			maioridade = idade
		if sexo == 'M' and idade > maioridade:
			nomevelho = nome
			maioridade = idade
		if sexo == 'F' and idade > 20:
			x = x + 1
	med = (s/4)
	print(f'Média de Idade do Grupo: {med}')
	print(f'O homem mais velho tem {maioridade} e seu nome é {nomevelho}')
	print(f'{x} mulher(es) tem(êm) mais de 20 anos.')
	
	
main()
