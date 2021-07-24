""" Desafio 025: """
# Programa Principal:
if __name__ == "__main__":
    # solicita que o usuário digite seu nome completo
    nome = input('Digite seu nome completo: ')
    
    # atribui à variável n a tupla que recebe o nome do usuário em caixa baixa e separado, cada elemento da tupla corresponde a um nome do usuário.
    n = nome.lower().split()
    
    # testa se no nome do usuário tem 'silva'
    teste = 'silva' in n
    
    # exibe se tem silva no nome. True para sim e False para não.
    print(f'Você tem Silva no seu nome? {teste}')
