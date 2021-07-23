""" Desafio 006: """

def linha():
    print('-'*25) # 25 caracteres - em sequência formando uma linha.

# Programa Principal:

if __name__ == "__main__":
    
    linha()
    n = float(input('Digite um número: ')) # entrada de um número em forma de caractere o qual será convertido para real dentro da função float(). 
    linha()
    
    raiz = n**(1/2) # n elevado a (1/2) => raiz quadrada de n.
    triplo = n * 3 # n multiplicado por três => triplo de n.
    dobro = n * 2 # n multiplicado por dois => dobro de n.
    
    print(f'O dobro de {n} é {dobro}, o triplo de {n} é {triplo} e a raiz de {n} é {raiz:.2f}')

