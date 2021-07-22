""" Desafio 017: """
from math import sqrt
# Programa Principal:

co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
h = sqrt(co**2 + ca**2)
print(f'A hipotenusa do Triângulo vale {h:.1f}.')
