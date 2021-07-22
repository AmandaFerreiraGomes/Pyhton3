""" Desafio 023: """

# Programa Principal:

num = input('Digite um número de 0 a 9999: ')
L = num.split()
print(f"""Unidade: {L[0][3]}
Dezena:  {L[0][2]}
Centena: {L[0][1]}
Milhar:  {L[0][0]}
""")
