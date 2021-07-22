""" Desafio 022: """
# Programa Principal

nome_completo = input('Digite seu nome completo: ')
print(nome_completo.upper())
print(nome_completo.lower())
nome = nome_completo.replace(' ', '')
print(f'Quantidade de Letras: {len(nome)}')
N = nome_completo.split()
print(f'Primeiro Nome: {N[0]}')
print(f'Quantidade de Letras no Primeiro Nome: {len(N[0])}')
