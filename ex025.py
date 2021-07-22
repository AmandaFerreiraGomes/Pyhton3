""" Desafio 025: """
# Programa Principal:

nome = input('Digite seu nome completo: ')
n = nome.lower().split()
teste = 'silva' in n
print(f'Você tem Silva no seu nome? {teste}')
