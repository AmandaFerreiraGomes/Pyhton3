""" Desafio 032: """
# Programa Principal:
print('-'*30)
ano = int(input('Digite o ano: '))
print('-'*30)
if ano % 4 == 0 and (ano % 400 == 0 or ano % 100 != 0):
	print(f'{ano} é BISSEXTO!')
else:
	print(f'{ano} não é BISSEXTO!')
