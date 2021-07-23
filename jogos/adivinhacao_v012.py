# CONCEITOS INTRODUTORIOS: IMPORT ..., RANDOM.RANDINT(A, B), FROM ... IMPORT ..., UM POUCO DE TRATAMENTO DE EXCEÇÕES

from random import randrange


def linha():
	print("--------------------------------------------")


def adivinhacao():
	linha()
	print("| Hello, bem-vindo ao Jogo de Adivinhação! |")
	
	linha()
	print("Selecione o nível de dificuldade:\n(1) FÁCIL\n(2) MÉDIO\n(3) DIFíCIL")
	linha()
	try:
		numero_secreto = randrange(1, 101)

		pontos = 0
		indice_tentativas = int(input("DIGITE A OPÇÃO: "))
		if indice_tentativas == 1:
			pontos = 1500
			tot_tentativas = 15
		elif indice_tentativas == 2:
			pontos = 1000
			tot_tentativas = 10
		elif indice_tentativas == 3:
			pontos = 500
			tot_tentativas = 5
			
		for rodada in range(0, tot_tentativas):
			
			print(f'Rodada {rodada + 1} de {tot_tentativas}')
			a = int(input("-> Digite um número natural entre 1 e 100: "))
			
			linha()
			print(f"-> Você digitou: {a}")
			linha()
			
			if a in range(1, 101):
				
				acertou = (a == numero_secreto)
				maior = (a > numero_secreto)
				menor = (a < numero_secreto)
				
				if acertou:
					linha()
					print("-> Parabéns! Você acertou!")
					linha()
					pontos = pontos + 1000
					break
				
				else:
					print("-> Que pena! Você errou!")
					pontos = pontos - 100
					print(f"Você tem {pontos} pontos.")
					if rodada == tot_tentativas:
						linha()
						print("-> Suas chances se esgotaram. Fim do Jogo!")
						linha()
					
					elif menor:
						print(f"{a} é menor!")
					
					elif maior:
						print(f"{a} é maior!")
			else:
				print("Você digitou um número inválido! Tente novamente com um número entre 1 e 100!")
				continue
		
		linha()
		print(f'Número Secreto: {numero_secreto}.')
		linha()
		
	except(KeyError, KeyboardInterrupt, Exception):
		linha()
		print("Comando Inválido!")
		linha()
	else:
		print("FIM DE JOGO!")
		print(f"Pontuação Final: {pontos}.")
		linha()


if __name__ == "__main__":
	adivinhacao()