""" Desafio 036: """


def main():
	print('\033[36m-------------------DADOS-------------------')
	valor = float(input('Digite o valor do imóvel: R$ '))
	salario = float(input('Digite o salário: R$ '))
	anos = int(input('Quantidade preterida de anos para quitar o financiamento: '))
	p = anos*12
	prestacao = (valor/p)
	if prestacao > (salario*0.3):
		print('\033[30mFINANCIAMENTO NEGADO!')
	else:
		print('\033[30mPARABÉNS! NÓS DO BANCO XXXXXX CONCEDEREMOS O FINANCIAMENTO DE SEU IMÓVEL.')
		print(f'\033[36mValor do Imóvel: {valor}\nQuantidade de Meses: {p}\nPrestação Mensal: {prestacao}.')
	
main()
