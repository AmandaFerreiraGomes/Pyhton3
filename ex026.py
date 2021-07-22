""" Desafio 026: """
# Programa Principal:

frase = input('Digite uma frase: ')
print(len(frase))
cont = frase.count('a')
pos = frase.find('a')
ult = (frase.rfind('a') + 1)
print(f'A letra ´a´ aparece {cont} vezes')
print(f'Primeira posição em que ´a´ fora encontrada: {pos}')
print(f'Última posição em que ´a´ fora encontrada: {ult}')
