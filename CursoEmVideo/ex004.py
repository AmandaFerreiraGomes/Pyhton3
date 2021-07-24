""" Desafio 004: """


def linha():
    print('-'*40)


if __name__ == '__main__':

    linha()
    # qualquer coisa deverá ser digitada pelo usuário
    n = input('Digite algo: ')
    linha()
    
    # identificará o que se relaciona a n, como tipo, se é numérico, alfánumérico, se está em caixa alta, se está em caixa baixa, se é um dígito, se possui espaço, se é um título...
    print(f'O tipo primitivo desse valor é {type(n)}')
    print(f'É alfabético e numérico? {n.isalnum()}')
    print(f'É apenas alfabético? {n.isalpha()}')
    print(f'Todos os caracteres são maiúsculos? {n.isupper()}')
    print(f'É possivel ser mostrado na tela? {n.isprintable()}')
    print(f'Faz parte do padrão ASCII? {n.isascii()}')
    print(f'É apenas numérico? {n.isnumeric()}')
    print(f'É um dígito? {n.isdigit()}')
    print(f'Todos os caracteres são espaços? {n.isspace()}')
    print(f'É um título? {n.istitle()}')
    print(f'Todos os caracteres são minúsculos? {n.islower()}')
