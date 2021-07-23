# CONCEITOS INTRODUTORIOS: WHILE, INCREMENTO E DECREMENTO

def linha():
	
	print("********************************************")


def main():
	
	linha()
	print("* Hello, bem-vindo ao Jogo de Adivinhação! *")
	linha()
	
	numero_secreto = 42
	tot_tentativas = 3
	rodada = 0
	
	linha()
	print(f"-> Você digitou: {numero_secreto}")
	linha()
	
	while (rodada < tot_tentativas):
		
		print(f'Rodada {rodada+1} de {tot_tentativas}')
		a = int(input("-> Digite um número do tipo inteiro: "))
		
		acertou = (a == numero_secreto)
		maior = (a > numero_secreto)
		menor = (a < numero_secreto)
		
		if (acertou):
			
			print("-> Parabéns! Você acertou!")
			break
		
		else:
			
			print("-> Que pena! Você errou!")
			
			if (menor):
				
				print(f"{a} é menor!")
			
			if (maior):
				
				print(f"{a} é maior!")
		
		rodada = rodada + 1
	
	linha()
	print("-> Suas chances se esgotaram. Fim do Jogo!")
	linha()


main()
