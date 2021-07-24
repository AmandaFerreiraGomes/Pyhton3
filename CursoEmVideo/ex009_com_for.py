# Desafio 009: 


def linha():
    print('-'*25)

def adicao(n):
    for i in range(0, 10):
        print(f'{n} + {i}  = {n + i}')
    

# função que tem como parâmetro n, o qual deverá ser um número do tipo inteiro definido pelo usuário.
def multiplicacao(n):
    # i é variável, a cada novo loop i = i + 1 até i = 9, já que o intervalo definido é [0, 10).
    for i in range(0, 10):
        print(f'{n} x {i}  = {n * i}')
        
    
# o usuário insere um número inteiro, o qual será utilizado para imprimir suas tabelas de adição/soma e de multiplicação.
if __name__ == "__main__":
    
    linha()
    n = int(input('Digite um número: '))
    linha()
    print(f'	TABUADA DE {n}')
    linha()
    print('		Multiplicação: ')
    multiplicacao(n) 
    linha()
    print('		Adição: ')
    adicao(n)
    linha()
