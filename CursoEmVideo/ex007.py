""" Desafio 007: """


def linha():
    print('-'*25) # 25 caracteres '-' concatenados formando uma linha

# Função que recebe dois parâmetros: nota1 e nota2 e retorna a média entre eles.

def media(nota1, nota2):
    med = ((nota1 + nota2)/2)
    return med

 # Programa Principal.

if __name__ == "__main__":
    
    linha()
    nota1 = float(input('Digite a Nota 1: ')) # nota 1 resultante da avaliação do tipo real
    nota2 = float(input('Digite a Nota 2: ')) # nota 2 resultante da avaliação do tipo real
    
    linha()
    print('Média: {:.1f}'.format( media(nota1, nota2)))
    linha()
