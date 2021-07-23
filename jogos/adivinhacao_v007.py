# CONCEITOS INTRODUTORIOS: IMPORT ..., RANDOM.CHOICE(RANGE(...)), IMPORT ...

import random as rd


def linha():
	print("********************************************")


def main():
	
	linha()
	print("* Hello, bem-vindo ao Jogo de Adivinhação! *")
	linha()
	
	numero_secreto = rd.choice(range(1, 101))
	tot_tentativas = 3
	
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

main()
