# CONCEITOS INTRODUTORIOS: ELIF, IGUALDADE, ATRIBUICAO, MAIOR_QUE, MENOR_QUE


def linha():
	print("********************************************")


def main():
	linha()
	print("* Hello, bem-vindo ao Jogo de Adivinhação! *")
	linha()
	
	a = int(input("-> Digite um número do tipo inteiro: "))
	
	numero_secreto = 42
	acertou = (a == numero_secreto)
	maior = (a > numero_secreto)
	menor = (a < numero_secreto)
	
	linha()
	print(f"-> Você digitou: {numero_secreto}")
	linha()
	
	if acertou:
		print("-> Parabéns! Você acertou!")
	else:
		print("-> Que pena! Você errou!")
		if menor:
			print(f"{a} é menor que {numero_secreto}!")
		if maior:
			print(f"{a} é maior que {numero_secreto}!")
	
	linha()
	print("-> Fim do Jogo!")
	linha()


main()
