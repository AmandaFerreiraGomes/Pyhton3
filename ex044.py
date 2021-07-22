""" Desafio 044: """
# Programa Principal:


def main():
	preco = float(input('Digite o preço do produto: R$ '))
	condicao = int(input("""Condição de Pagamento:
	1 - À VISTA(DINHEIRO OU CHEQUE).
	2 - À VISTA NO CARTÃO.
	3 - DUAS PARCELAS NO CARTÃO.
	4 - TRÊS PARCELAS OU MAIS."""))
	if condicao == 1:
		pagamento = (preco - (preco*0.1))
		print(f'Preço: R$ {pagamento}.\nCom desconto de 10%.')
	elif condicao == 2:
		pagamento = (preco - (preco*0.05))
		print(f'Preço: R$ {pagamento}.\nCom desconto de 5%')
	elif condicao == 3:
		pagamento = preco / 2
		print(f'2 x de R$ {pagamento}.')
	elif condicao == 4:
		vezes = int(input('Quantidade de Parcelas: '))
		if vezes>2:
			pagamento = ((preco + (preco*0.2))/vezes)
			print(f'{vezes} x de R$ {pagamento}')
		else:
			print('Escolha a Condição 3.')
		
	else:
		print('Opção Inválida!')
	

main()
