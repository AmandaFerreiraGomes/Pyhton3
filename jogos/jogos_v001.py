# MENU DO JOGO


from adivinhacao_v012 import adivinhacao
from forca_v001 import forca


def linha():
	print("-------------------------------------------")
	pass


def cabecalho():
	linha()
	print("| Hello, bem-vindo ao Menu de Jogos! |")
	linha()
	

def main():
	cabecalho()
	try:
		opcao = int(input("Selecione o jogo que deseja jogar:\n (1) - Jogo de Adivinhação\n (2) - Jogo da Forca\n--------------------------------------------\n"))
		if opcao == 1:
			adivinhacao()
		elif opcao == 2:
			forca()
		else:
			print("Valor Inválido!")
	except:
		print("Opção Inválida!")
	

if __name__ == "__main__":
	main()