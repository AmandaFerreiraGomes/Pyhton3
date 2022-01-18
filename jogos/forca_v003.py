from random import choice


def cabecalho():
    print('*******************************')
    print('* Bem-vindo ao jogo da Forca! *')
    print('*******************************')


def carrega_palavra():

    # define-se o caminho do arquivo que será acessado
    path = 'C:/Users/AmandaGomes-OSBR/Desktop/ESTUDOS/PYTHON/frutas.txt'
    
    # abre-se o arquivo para leitura
    with open(path, 'r') as arquivo:
        palavras = [linha.strip() for linha in arquivo]
    
    # cria-se uma lista, que lê linha por linha e remove os caracteres especiais que possam estar contidos nessas linhas 
    return palavras


def inicializa_jogo(palavra):
    
    # lista que recebe len(palavra) de caracteres '_'
    letras_acertadas = ['_' for i in range(0, len(palavra))]
    
    print(f'A palavra secreta possui {len(palavra)} caracteres e a categoria é fruta.')

    # imprime os '_'
    for caractere in letras_acertadas:
        print(f'{caractere}', end=' ')
    print('\n')
    return letras_acertadas


def forca():
    
    # variável que guarda a palavra secreta, que foi sorteada com o método choice da biblioteca random
    palavras = carrega_palavra()
    secret = choice(palavras).upper()
    chute = ''
    letras_acertadas = list()
    qtd_chances = 13
    tentativa = 0

    # lista preenchida com caracteres '_'
    letras_acertadas = inicializa_jogo(secret)

    try:
        while True:

            tentativa += 1
            print(f'---- Tentativa {tentativa} de {qtd_chances}: ----')
            chute = input('Digite uma letra: ').strip().upper()
            index = 0
            contagem = []

            for letter in secret:
                if chute == letter:
                    letras_acertadas[index] = chute
                index += 1
                contagem.append(letras_acertadas.count(chute))
            
            if '_' not in letras_acertadas:
                print(f'{secret}.\nVocê venceu!')
                break
            elif tentativa == qtd_chances:
                print(f'Você perdeu! A palavra era {secret}.')
                break
            
            for item in letras_acertadas:
                print(f' {item} ', end='')
            print('\n')    
    except Exception as e:
        print(type(e))
        

if __name__ == '__main__':

    cabecalho()
    forca()

