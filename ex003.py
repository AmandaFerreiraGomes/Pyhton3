""" Desafio 003: """

# Definição da função soma:

def soma():
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro: '))
    s = n1 + n2
    
    print(f'A soma entre {n1} e {n2} vale {s}.') # Usando o format de um jeito diferente do .format(...) 
    print(f'{n1} + {n2} = {s}') # Por padrão, o tab tem de ser de 4 espaços.

# Programa Principal:

if __name__ == "__main__":
    soma()

