""" Desafio 012: """


def linha():
    print('-'*25)

    
if __name__ == "__main__":
    
    # cabeçalho:
    linha()
    print('		DESCONTOS: ')
    linha()
    
    # inserção de dado preço
    preco = float(input('Preço: R$ '))
    
    # cálculo do desconto:
    desc = preco*0.05 # desconto de 5%
    final = preco - desc # preço final, sendo preço - desconto de 5% sobre preço
    
    # exibição do preço final:
    print(f'-> Com o desconto de R$ {desc:.2f}, o produto passa a custar R$ {final:.2f}')
