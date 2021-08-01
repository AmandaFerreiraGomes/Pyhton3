""" Desafio 046: """
# Programa Principal:
import time, emoji


def contagem(): # contagem regressiva para a virada do ano (são dez segudos).
	for e in range(10, 0, -1):
		print(f'{e}')
		time.sleep(1)


if __name__ == "__main__":
	
	contagem()
	print(4*emoji.emojize(':fireworks:')) # exibe 4 emojis de fogos de artifício.

	
