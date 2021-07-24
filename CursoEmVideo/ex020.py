""" Desafio 020: """


# importando da biblioteca random a função shuffle, a qual é utilizada para embaralhar os dados. Exemplo: L = [1, 2, 3, 4] => s = suffle(L) => s = [2, 3, 4, 1].
from random import shuffle


def linha():
    print('-' * 30)
    
    
# Programa Principal
if __name__ == "__main__":
    
    # cabeçalho
    linha()
    print('		SEQUÊNCIA DO SORTEIO')
    linha()
    
    #entrada dos valores que serão inseridos na tupla L
    n1 = input('Digite o nome do aluno 1: ')
    n2 = input('Digite o nome do aluno 2: ')
    n3 = input('Digite o nome do aluno 3: ')
    n4 = input('Digite o nome do aluno 4: ')
    
    # atribuição da tupla [n1, n2, n3, n4] à L
    L = [n1, n2, n3, n4]
 
    # L é embaralhado
    shuffle(L)
    
    # exibição do resultado, de L embaralhado
    print(f'A ordem de sorteio foi {L}.')

