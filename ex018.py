""" Desafio 018: """
from math import sin, cos, tan

# Programa Principal:
print('-'*30)
a = int(input('Digite a medida do ângulo em radianos: '))
s = sin(a)
c = cos(a)
t = tan(a)
print('-'*30)
print(f'-> Seno: {s:.2f}\n-> Cosseno: {c:.2f}\n-> Tangente: {t:.2f}.')
print('-'*30)
