""" Desafio 069: """
# Programa Principal:


def main():
	x = y = z = 0
	cond = sexo = ''
	while True:
		if sexo != 'F' or sexo != 'M':
			while True:
				sexo = str(input('Sexo [M/F]: ')).strip().upper()
				if sexo == 'F' or sexo == 'M':
					break
		idade = int(input('Digite sua idade: '))
		if idade > 18:
			x = x + 1
		if sexo in 'Mm':
			y += 1
		if sexo in 'Ff' and idade > 20:
			z += 1
		if cond != 'S' or cond != 'N':
			while True:
				cond = str(input('Você deseja parar?[S/N].')).upper()
				if cond == 'S' or cond == 'N':
					print('Programa Finalizado!')
					break
			break
	print(f"""{x} pessoa(s) tem(êm) mais de 18 anos.\n{y} pessoa(s) é(são) do sexo masculino.
{z} pessoa(s) é(são) do sexo feminino e tem(êm) mais de 20 anos.""")


main()
