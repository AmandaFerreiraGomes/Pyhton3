""" Desafio 092: """
from datetime import datetime
# Programa Principal:


def main():
	print('=-'*13)
	print('CONSULTA DE APOSENTADORIA')
	print('=-' * 13)
	dados = dict()
	dados['Nome'] = str(input('Nome: '))
	nascimento = int(input('Ano de Nascimento: '))
	dados['Sexo'] = str(input('Sexo[M/F]: ')).upper()
	idade = datetime.now().year - nascimento
	dados['Idade'] = idade
	dados['CTPS'] = int(input('CTPS: '))
	if dados['CTPS'] != 0:
		dados['Contraração'] = int(input('Ano de Contratação: '))
		dados['Salário'] = float(input('Salário: R$ '))
		if dados['Sexo'] == 'M':
			v = 35
		elif dados['Sexo'] == 'F':
			v = 30
		dados['Aposentadoria'] = (dados['Contraração'] - nascimento) + v
		for k, v in dados.items():
			print(f'{k} -> {v}.')
	else:
		for k, v in dados.items():
			print(f'{k} -> {v}')
	print('-=-' * 7)
	print(' Consulta Finalizada!')
	print('-=-' * 7)


main()
