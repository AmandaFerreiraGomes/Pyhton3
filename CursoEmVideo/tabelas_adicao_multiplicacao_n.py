""" Desafio 009: """
# subtende-se que ainda não tinha conhecimento de for.

def linha():
    print('-'*25)

def adicao(n):
    print(f'{n} + 0  = {n + 0}')
    print(f'{n} + 1  = {n + 1}')
    print(f'{n} + 2  = {n + 2}')
    print(f'{n} + 3  = {n + 3}')
    print(f'{n} + 4  = {n + 4}')
    print(f'{n} + 5  = {n + 5}')
    print(f'{n} + 6  = {n + 6}')
    print(f'{n} + 7  = {n + 7}')
    print(f'{n} + 8  = {n + 8}')
    print(f'{n} + 9  = {n + 9}')
    
   
def multiplicacaop(n):
    print(f'{n} x 0  = {n*0}')
    print(f'{n} x 1  = {n*1}')
    print(f'{n} x 2  = {n*2}')
    print(f'{n} x 3  = {n*3}')
    print(f'{n} x 4  = {n*4}')
    print(f'{n} x 5  = {n*5}')
    print(f'{n} x 6  = {n*6}')
    print(f'{n} x 7  = {n*7}')
    print(f'{n} x 8  = {n*8}')
    print(f'{n} x 9  = {n*9}')
    
    
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
