""" Desafio 035: """
import math
# Programa Principal:
a = float(input('Digite o tamanho do segmento de reta(em cm): '))
b = float(input('Digite o tamanho do segmento de reta(em cm): '))
c = float(input('Digite o tamanho do segmento de reta(em cm): '))
if (abs(b-c) < a < c + b) and (abs(a-c) < b < a + c) and (abs(a-b) < c < a + b):
	print('Sim, eles podem formar um TRIÂNGULO!')
else:
	print('Não, eles não podem formar um TRIÂNGULO!')
