""" Desafio 029: """


def linha():
    print('-' * 30)


# Programa Pricipal:
if __name__ == "__main__":
    # o usuário insere a velocidade em quilômetros:
    linha()
    v = float(input('Velocidade(km/h): '))
    linha()
     
    # se a velociadade for maior que 80 km/h, então o veículo será multado. A multa é calculada com o valor acima do permitido multiplocado por 7, ou seja, sete reais para cada km/h acima do permitido
    if v > 80:
        multa = (v-80)*7
        print(f'Você foi multado(a) em R$ {multa:.2f}.')
    # caso contrário, o motorista é parabenizado por não ultrapassar o limite de velocidade e não é multado
    else:
        print('Parabéns! Você respeita as normas de trânsito!')
    linha()
