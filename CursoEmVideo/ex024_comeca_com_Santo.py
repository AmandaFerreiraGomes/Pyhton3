""" Desafio 024: """


# Programa Principal:
if __name__ == "__main__":
    
    # solicita entre com o dado nome de uma cidade:
    nome = input('Nome de uma Cidade: ')
    
    # o nome da cidade é separado onde tem espaço e forma a tupla L
    L = nome.split()
    
    # verifica se o primeiro nome da cidade é 'Santo'
    b = 'Santo' in L[0] 
    
    # Se começar com 'Santo' retorna True, caso contrário retorna False
    print(f'O nome começa com SANTO? {b}')
