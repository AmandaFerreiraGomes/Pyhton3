def menu():
	print("""\t\tCondição de Pagamento:
	
1 - À VISTA(DINHEIRO OU CHEQUE).
2 - À VISTA NO CARTÃO.
3 - DUAS PARCELAS NO CARTÃO.
4 - TRÊS PARCELAS OU MAIS.
""".upper(), end='')


def linha():
	print('-'*36)


def condicao():
	print('\033[36m', end='')
	cond = int(input('-> Opção: '.upper()))
	print('\033[m', end='')
	return cond


def pagamento(cond, preco):
	
	condicao = cond
	pag = 0 # valor cobrado no final
	desconto = 0 # desconto sobre o preco do produto
	acrescimo = 0
	vez = 0
	
	if condicao == 1:
		desconto = 10
		pag = (preco - (preco * (desconto/100)))
		vez = 1
	elif condicao == 2:
		desconto = 5
		pag = (preco - (preco * (desconto/100)))
		vez = 1

	elif condicao == 3:
		pag = preco / 2
		desconto = 0
		vez = 2
		
	elif condicao == 4:
		
		print ('\033[36m', end='')
		vezes = int(input('-> Quantidade de Parcelas: '.upper()))
		print('\033[m', end='')
		linha()
		
		if vezes > 2:
			acrescimo = 20
			pag = ((preco + (preco * (acrescimo/100))) / vezes)
			vez = vezes
		
		
		else:
			print('Escolha a Condição 3.')
	
	else:
		print('Opção Inválida!')
		
	print(f'PAGAMENTO: {vez} x de R$ {pag:.2f}.\nCom desconto de {desconto}%.\nCom acréscimo de {acrescimo}%.'.upper())

# Programa Principal:
if __name__ == "__main__":
	
	try:
		linha()
		print(' BEM-VINDO AO SISTEMA PAGAMENTO V2.0!') # cabecalho
		linha()
		
		print('\033[36m', end='') # imprime a solicitacao abaixo na cor verde, finaliza a string sem espaco e sem new line
		preco = float(input('-> Digite o preço do produto: R$ \033[m'.upper()))
		print('\033[m', end='') # remove a cor verde da continuacao do programa
		linha()
		
		menu() # menu de opcoes, as quais o usuario podera escolher
		linha()
		
		cond = condicao() # a variavel cond recebe o retorno da funcao condicao, na qual o usuario insere a opcao desejada de acordo com o que esta escrito no menu
		linha()
		
		pagamento(cond, preco) # funcao que recebe dois parametros, os quais serao a base para o calculo da forma de pagamento do cliente, dos descontos e dos acrescimos sobre o preco do produto.
		linha()
	
	except (KeyboardInterrupt, KeyError, ValueError):
		print("\033[31mERRO NA EXECUÇÃO DO PROGRAMA!")

