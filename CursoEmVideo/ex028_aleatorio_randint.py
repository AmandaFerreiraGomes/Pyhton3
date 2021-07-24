""" Desafio 028: """


from random import randint


# Programa Principal:
if __name__ == '__main__':
    # x recebe um valor aleatório entre 0 e 5: [0, 5).
    x = randint(0, 5)
    
    # o usuário digita um número
    num = int(input('Digite um número inteiro(0 a 5): '))
    if num == x:
        print('VOCÊ VENCEU!')
    else:
        print('VOCÊ PERDEU')
    print(f'O número sorteado foi {x}')
