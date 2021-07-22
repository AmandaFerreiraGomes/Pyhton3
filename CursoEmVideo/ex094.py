""" Desafio 094: """
# Programa Principal:


def main():
	cond = 'S'
	dicionario = dict()
	lista = list()
	listam = []
	listamaiores = []
	s = x = 0
	while True:
		if cond == 'S':
			x = x + 1
			dicionario['Nome'] = str(input('Nome: '))
			dicionario['Sexo'] = str(input('Sexo[M/F]: ')).upper()
			while dicionario['Sexo'] not in 'MF':
				dicionario['Sexo'] = str(input('Sexo[M/F]: ')).upper()
			dicionario['Idade'] = int(input('Idade: '))
			s += dicionario['Idade']
			if dicionario['Sexo'] == 'F':
				listam.append(dicionario['Nome'])
			lista.append(dicionario.copy())
			cond = str(input('Deseja continuar [S/N]? ')).upper()
		elif cond == 'N':
			med = (s/x)
			print(f'\033[7:30:44m-> Média de Idade: {med:.1f} \033[m')
			for i in listam:
				print(f'\033[7:30:44m-> Mulheres Cadastradas: {i} \033[m')
			for i in lista:
				if i['Idade'] >= med:
					listamaiores.append(i['Nome'])
			
			print('Idade Acima da Média: ', end='')
			for k in listamaiores:
				print(f'{k}', end='')
			print()
			print(f'\033[7:30:44m-> Quantidade de Cadastros: {x} \033[m')
			print('\033[30:44m-=\033[m'*12)
			print('\033[1:31:40m<<Fim da Execução>>\033[m')
			print('\033[30:44m-=\033[m'*12)
			break
		else:
			print('Condição Inválida!')
			cond = str(input('Deseja continuar [S/N]? ')).upper()


main()
