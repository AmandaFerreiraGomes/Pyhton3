
""" Desafio 002: """


def azul():
    cores = {
        'azul': '\033[34m'
    }
    return cores['azul']

if __name__ == '__main__':
    a = input('Digite seu nome: ')
    print(f'É um prazer te conhecer, {azul()}{a}!')
