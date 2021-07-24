""" Desafio 022: """


def linha():
    print('-' * 40)


# Programa Principal
if __name__ == "__main__":
    # solicita que o usuário digite seu nome completo
    linha()
    nome_completo = input('Digite seu nome completo: ')
    linha()
    # exibe em tela o nome digitado pelo usuário em caixa alta
    print(nome_completo.upper())
    
    # exibe o nome digitado pelo usuário em caixa baixa
    print(nome_completo.lower())
    
    # atribui à variável nome o nome do usuário em que os espaços ' ' são substituídos por ','
    nome = nome_completo.replace(' ', '')
    
    # exibe a quantidade de letras que nome possui
    print(f'Quantidade de Letras: {len(nome)}')
    
    # N recebe a tupla resultante da separação dos nomes do usuário feitas pela função split
    N = nome_completo.split()
    
    # exibe o primeiro nome, que é o primeiro elemento da tupla N
    print(f'Primeiro Nome: {N[0]}')
    
    # exibe a quantidade de letras do primeiro elemento da tupla N, que é o primeiro nome do usuário
    print(f'Quantidade de Letras no Primeiro Nome: {len(N[0])}')
