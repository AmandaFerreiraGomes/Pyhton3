# JOGO DA FORCA:


def linha():
	print("********************************************")


def forca():
	linha()
	print("* Hello, bem-vindo ao Jogo da Forca! *")
	linha()
	
	try:
		palavra = 'banana'

		enforcou = False
		acertou = False
		pontuacao = 0

		while (not enforcou) and (not acertou):
			chute = input("Digite uma letra: ")
			
	except (KeyboardInterrupt, KeyError):
		print("Entrada Inválida!")


if __name__ == "__main__":
	forca()