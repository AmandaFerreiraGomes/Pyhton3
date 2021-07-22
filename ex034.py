""" Desafio 034: """


def azul():
	return '\033[34m'


# Programa Principal:
branco = '\033[30m'
salario = float(input('Qual o valor do seu salário? R$ '))
if salario > 1250.00:
	n_s = salario + (salario * 0.10)
else:
	n_s = salario + (salario * 0.15)
print(f'{azul()}-'*30)

print(f'{branco}Novo salário: R$ {n_s:.2f}. Aumento: R$ {n_s-salario:.2f}.')
