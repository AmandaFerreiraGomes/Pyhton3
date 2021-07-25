""" Desafio 036: """


def linha():
	print('-' * 43)


if __name__ == "__main__":
	
	# cabeçalho:
	linha()
	print('\033[36m-------------------DADOS-------------------\033[m')
	linha()
	
	# inserção de dados pelo usuário:
	valor = float(input('Digite o valor do imóvel: R$ '))
	salario = float(input('Digite o salário: R$ '))
	anos = int(input('Quantidade preterida de anos para quitar o financiamento: '))
	
	# p é a quantidade de prestações nos anos. Ex.: 2 anos => 24 prestações
	p = anos * 12
	
	# prestacao se refere à quantidade que será para. Se o valor for 24000, então a prestação será de 2000 por mês.
	prestacao = (valor / p)
	
	# se o valor da prestação for maior que 30% do salário, então o financiamento é negado.
	linha()
	if prestacao > (salario * 0.3):
		print('\033[31mFINANCIAMENTO NEGADO!\033[m')
	# caso contrário, o financiamento é aceito e são exibidas os dados do financiamento.
	else:
		print('\033[30mPARABÉNS! NóS DO BANCO XXXXXX CONCEDEREMOS O FINANCIAMENTO DE SEU IMóVEL.')
		print(
			f'\033[36mValor do Imóvel: R$ {valor:.2f}\nQuantidade de Meses: {p}\nPrestação Mensal: R$ {prestacao:.2f}.')
	
	linha()
