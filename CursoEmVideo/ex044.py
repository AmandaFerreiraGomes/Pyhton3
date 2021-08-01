""" Desafio 044: """


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
	
	cond = int(input('Opção: '.upper()))
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
		
		vezes = int(input('Quantidade de Parcelas: '.upper()))
		
		if vezes > 2:
			acrescimo = 20
			paga = ((preco + (preco * (acrescimo/100))) / vezes)
			vez = vezes
		
		
		else:
			print('Escolha a Condição 3.')
	
	else:
		print('Opção Inválida!')
		
	print(f'Preço: {vez} x de R$ {pag:.2f}.\nCom desconto de {desconto}%\nCom acréscimo de {acrescimo}%'.upper())


# Programa Principal:
if __name__ == "__main__":
	
	try:
		linha()
		print(' BEM-VINDO AO SISTEMA DESCONTO V2.0 ')
		linha()
		
		preco = float(input('-> Digite o preço do produto: R$ '.upper()))
		linha()
		
		menu()
		linha()
		
		cond = condicao()
		linha()
		
		pagamento(cond, preco)
		linha()
	
	except (KeyboardInterrupt, KeyError, ValueError):
		print("\033[31mERRO NA EXECUÇÃO DO PROGRAMA!")
	
