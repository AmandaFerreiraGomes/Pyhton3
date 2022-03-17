
""" Desafio 002: """


def azul() -> str :
    cores : dict = {
        'azul': '\033[34m'
    }
    return cores['azul']

if __name__ == '__main__':
    a : str = input('Digite seu nome: ')
    print(f'É um prazer te conhecer, {azul()}{a}!')
