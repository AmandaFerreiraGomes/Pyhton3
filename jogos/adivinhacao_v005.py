# CONCEITOS INTRODUTORIOS: FOR, RANGE, BREAK, IN

def linha():
	print("********************************************")


def main():
	linha()
	print("* Hello, bem-vindo ao Jogo de Adivinhação! *")
	linha()
	
	numero_secreto = 42
	tot_tentativas = 3
	
	linha()
	print(f"-> Você digitou: {numero_secreto}")
	linha()
	
	for rodada in range(0, tot_tentativas):
		
		print(f'Rodada {rodada + 1} de {tot_tentativas}')
		a = int(input("-> Digite um número do tipo inteiro: "))
		
		acertou = (a == numero_secreto)
		maior = (a > numero_secreto)
		menor = (a < numero_secreto)
		
		if (acertou):
			
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
	
			elif (maior):
				print(f"{a} é maior!")
				


main()
