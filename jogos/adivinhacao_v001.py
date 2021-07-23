#CONCEITOS INTRODUTORIOS: IF, ELSE

def linha():
	print("********************************************")


def main():
	
	linha()
	print("* Hello, bem-vindo ao Jogo de Adivinhação! *")
	linha()

	numero_secreto = 42
	
	a = int(input("Digite um número do tipo inteiro: "))
	linha()
	
	print(f"Você digitou {numero_secreto}")
	
	if a == numero_secreto:
		print("Parabéns! Você acertou!")
	else:
		print("Que pena! Você errou!")


main()
