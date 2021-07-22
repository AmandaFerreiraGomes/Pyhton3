""" Desafio 046: """
# Programa Principal:
import time, emoji


def main():
	for e in range(10, 0, -1):
		print(f'{e}')
		time.sleep(1)
	print(4*emoji.emojize(':fireworks:'))
	

main()
