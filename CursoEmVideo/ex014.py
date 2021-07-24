""" Desafio 014: """


def linha():
    print('-'*45)


# Programa Principal:
if __name__ == "__main__":
    # cabeçalho:
    linha()
    print('	  CONVERSÃO DE TEMPERATURA: ºC -> ºF.')
    linha()
    
    # entrada do valor da temperatura em graus celsius:
    c = float(input('Digite a temperatura em graus Celsius(ºC): '))
    
    # cálculo de conversão de celsius para fahrenheit:
    f = ((9*c + 160)/5)
    
    # exibição do resultado da conversão:
    linha()
    print(f'	-> {c:.1f}ºC correspondem a {f:.1f}ºF.')
    linha()
