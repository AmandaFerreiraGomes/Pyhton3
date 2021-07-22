""" Desafio 097: """
# Funções Personalizadas:


def escreva(msg):
	x = (len(msg)//2)+1
	print('-='*x)
	print(f' {msg} ')
	print('-='*x)


# Programa Principal:


def main():
	mensagem = str(input('MENSAGEM: '))
	escreva(mensagem)


main()
