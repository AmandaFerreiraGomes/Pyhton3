""" Desafio 005: """

# Programa Principal:

if __name__ == '__main__':
    
    n = int(input('Digite um número: ')) # solicita  a entrada de um número, o qual entra como caractere e é convertido para inteiro.
    
    a = n - 1 # antecessor de n
    s = n + 1 # sucessor de n
    # exemplo: para n = 10 => a = 9; s = 11.
    
    print('O antecessor de {} é {} e seu sucessor é {}'.format(n, a, s)) # método 1 de usar o format
    
    print(f'O antecessor de {n} é {n-1} e seu sucessor é {n + 1}') # método 2 de usar o format. *método de minha preferência, inclusive.
