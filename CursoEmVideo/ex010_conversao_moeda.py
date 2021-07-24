""" Desafio 010: """


def linha():
    print('-'*50)

if __name__ == "__main__":
    # cabecalho:
    linha()
    print('				Compra de Dólar:')
    linha()
    
    # interação com o usuário:
    dinheiro = float(input('Quantos reais você tem na carteira? R$ '))
    cot = float(input('Cotação atual do dólar(em R$): '))
    
    # cálculo de conversão
    dolar = (dinheiro/cot)
    
    # exibição do resultado:
    linha()
    print(f'Você pode comprar US$ {dolar:.2f}.')
    linha()
