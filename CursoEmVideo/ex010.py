""" Desafio 010: """

print('-'*50)
print('				Compra de Dólar:')
print('-'*50)
dinheiro = float(input('Quantos reais você tem na carteira? R$ '))
cot = float(input('Cotação atual do dólar(em R$): '))
dolar = (dinheiro/cot)
print('-'*30)
print(f'Você pode comprar US$ {dolar:.2f}.')
print('-'*30)