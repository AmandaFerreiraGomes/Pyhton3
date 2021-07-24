""" Desafio 013: """


def linha():
    print('-' * 24)


if __name__ == "__main__":
    # cabeçalho:
    linha()
    print('    AUMENTO SALARIAL    ')
    linha()
    
    # inserção do salário atual, o qual será a base do cálculo:
    salario = float(input('Digite seu salário: '))
    
    # cálculo do aumento salarial de 15%
    aumento = salario*0.15 # valor do aumento de 15%
    final = salario + aumento # acréscimo de 15% ao salário atual.
    
    # exibição do resultado do aumento salarial.
    print(f'Com um aumento de 15%, seu novo salário passa a ser de R$ {final:.2f}.')
