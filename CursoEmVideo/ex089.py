""" Desafio 089: """
# Programa Principal:


def main():
	cond = 'S'
	aluno = []
	todos = []
	med = []
	while True:
		if cond == 'N':
			break
		elif cond == 'S':
			nome = str(input('Nome: '))
			nota1 = float(input('Nota 1: '))
			nota2 = float(input('Nota 2: '))
			aluno.append(nome)
			aluno.append(nota1)
			aluno.append(nota2)
			cond = str(input('Deseja continuar [S/N]? ')).upper()
		else:
			print('Comando Inválido!')
			cond = str(input('Deseja continuar [S/N]? ')).upper()
		todos.append(aluno[:])
		aluno.clear()
	for e in todos:
		media = (e[1] + e[2]) / 2
		med.append(media)
	id = 'ALUNO'
	note = 'MÉDIA'
	name = 'NOME'
	print('-' * 30)
	print(f'\033[30:44m{id:^7}| {name:^15}| {note:^6}\033[m')
	for x, n in enumerate(todos):
		print(f'{x:^7}| {n[0]:^15}| {med[x]:>4}')
	print('-'*30)
	x = 0
	cond = 'S'
	while True:
		if cond == 'N' or x == len(todos):
			print('Programa Finalizado!')
			break
		elif cond not in 'SN':
			print('Condição Inválida!')
			cond = str(input('Deseja continuar[S/N]? ')).upper()
		else:
			mostrar = int(input('Digite o número do aluno: '))
			c = mostrar
			print(f'-> {todos[c][0]}: [{todos[c][1]}, {todos[c][2]}]')
			cond = str(input('Deseja mostrar outra nota[S/N]? ')).upper()
		x = x + 1


main()
