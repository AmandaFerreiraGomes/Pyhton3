""" Desafio 026: """


# Programa Principal:
if __name__ == "__main__":
    # solicita que uma frase seja inserida
    frase = input('Digite uma frase: ')
    
    # exibe o tamanho da frase, como não tem nenhuma remoção dos espaços em branco, a função len() contará com eles em seus cálculos
    print(len(frase))
    
    # conta quantas letras 'a' minúsculas tem na frase
    cont = frase.count('a')
    
    # encontra a posição da primeira letra 'a' na frase
    pos = frase.find('a')
    
    # encontra a posição da última letra 'a' na frase
    ult = (frase.rfind('a') + 1)
    
    # exibe a quantidade de letras 'a' na frase:
    print(f'A letra ´a´ aparece {cont} vezes')
    
    # exibição em tela de:
    print(f'Primeira posição em que ´a´ fora encontrada: {pos}')
    print(f'Última posição em que ´a´ fora encontrada: {ult}')
