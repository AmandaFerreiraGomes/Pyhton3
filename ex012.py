""" Desafio 012: """
print('-'*25)
print('		DESCONTOS: ')
print('-'*25)
preco = float(input('Preço: R$ '))
print('-'*25)
desc = preco*0.05
final = preco - desc
print(f'-> Com o desconto de {desc:.2f}, o produto passa a custar {final:.2f}')
print('-'*25)
