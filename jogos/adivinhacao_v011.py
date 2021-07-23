# CONCEITOS INTRODUTORIOS: IMPORT ..., RANDOM.RANDINT(A, B), FROM ... IMPORT ..., UM POUCO DE TRATAMENTO DE EXCEÇÕES

from random import randrange


def linha():
	print("--------------------------------------------")


def main():
	
	linha()
	print("| Hello, bem-vindo ao Jogo de Adivinhação! |")
	
	numero_secreto = randrange(1, 101)
	
	linha()
	print("Selecione o nível de dificuldade:\n(0) FÁCIL\n(1) MÉDIO\n(2) DIFíCIL")
	linha()
	try:
		indice_tentativas = int(input("DIGITE A OPÇÃO: "))
		if indice_tentativas == 0:
			tot_tentativas = 5
		elif indice_tentativas == 1:
			tot_tentativas = 10
		elif indice_tentativas == 2:
			tot_tentativas = 15
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
					
					break
				
				else:
					print("-> Que pena! Você errou!")
					
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
	except (KeyboardInterrupt, Exception):
		linha()
		
		print("Comando Inválido!")
		
	linha()
	print("FIM DE JOGO!")
	

main()
