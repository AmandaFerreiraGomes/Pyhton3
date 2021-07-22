""" Desafio 015: """

# Programa Principal
print('-'*30)
print('		ALUGUEL DE CARROS')
print('-'*30)
km = float(input('-> Quantidade de quilômertos percorridos: '))
dias = int(input('-> Dias de uso: '))
print('-'*60)
p = ((60*dias) + (0.15*km))

print(f'O custo total por {dias} dias e {km:.2f} km rodados é de R$ {p:.2f}.')
print('-'*60)
