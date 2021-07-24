""" Desafio 003: """

# Definição da função soma:

def soma(n1, n2):
    s = n1 + n2
    

# Programa Principal:

if __name__ == "__main__":
    
    # entrada dos valores n1 e n2
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro: '))
    
    # chamada da função soma, a qual recebe os parâmetros n1 e n2
    soma(n1, n2)
    
    # exibição do resultado da operação soma
    print(f'A soma entre {n1} e {n2} vale {s}.') # Usando o format de um jeito diferente do .format(...) 
    print(f'{n1} + {n2} = {s}') # Por padrão, o tab tem de ser de 4 espaços.
