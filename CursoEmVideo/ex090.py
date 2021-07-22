""" Desafio 090: """
# Programa Principal:


def main():
	dados = dict()
	dados['nome'] = str(input('Nome: '))
	dados['media'] = float(input('Média: '))
	if dados['media'] >= 7.0:
		print(f'{dados["nome"]} aprovado(a) com média {dados["media"]}!')
	else:
		print(f'{dados["nome"]} reprovado(a) com média {dados["media"]}!')


main()
