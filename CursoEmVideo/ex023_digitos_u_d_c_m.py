""" Desafio 023: """


# Programa Principal:
if __name__ == "__main__":
  
    # solicita que o usuário digite um número no intervalo [0, 9999], o qual será do tipo caractere
    num = input('Digite um número de 0 a 9999: ')
    
    # separa cada dígito do número digitado
    L = num.split()
    
    # exibe o primeiro elemento da tupla L, em que [0][3] é o dígito da unidade, [0][2] é o dígito da dezena, [0][1] é o dígito da centena, [0][0] é o dígito do milhar.
    print(f"""
    Unidade: {L[0][3]}
    Dezena:  {L[0][2]}
    Centena: {L[0][1]}
    Milhar:  {L[0][0]}
    """)
