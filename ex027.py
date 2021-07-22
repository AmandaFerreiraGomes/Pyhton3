""" Desafio 027: """
# Programa Principal:

nome_completo = input('Digite seu nome completo: ')
nome = nome_completo.split()
x = len(nome) - 1
print(f'Primeiro nome: {nome[0]}')
print(f'Último nome: {nome[x]}')

