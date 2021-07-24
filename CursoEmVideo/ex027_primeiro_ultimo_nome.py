""" Desafio 027: """


# Programa Principal:
if __name__ == '__main__':
    
    # pede que o usuário insira o nome completo
    nome_completo = input('Digite seu nome completo: ')
    
    # coloca o nome do usuário em uma tupla(a tupla nome), em que cada nome corresponde a um elemento
    nome = nome_completo.split()
    
    # atrbui à variável x o tamanho da tupla -1 porque a tupla começa a contagem no índice zero
    x = len(nome) - 1
    
    # exibe o primeiro elemento da tupla, que é o primeiro nome do usuário
    print(f'Primeiro nome: {nome[0]}')
    
    # exibe o último elemento da tupla que é o último nome do usuário
    print(f'Último nome: {nome[x]}')

