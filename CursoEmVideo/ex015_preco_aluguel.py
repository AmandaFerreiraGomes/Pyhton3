""" Desafio 015: """
 

# linha com 30 caracteres
def linha30():
    print('-' * 30)


# linha com 60 caracteres
def linha60():
    print('-' * 60)
    
    
# Programa Principal
if __name__ == "__main__":
    
    # cabeçalho:
    linha30()
    print('		ALUGUEL DE CARROS')
    linha30()
    
    # inserção da quantidade de kms percorridos e dos dias de uso do automóvel.
    km = float(input('-> Quantidade de quilômertos percorridos: '))
    dias = int(input('-> Dias de uso: '))
    
    # cálculo do preço do aluguel do veículo, 60 reais cobrados por dia de uso + 15 centavos cobrados por quilômetros percorridos
    p = ((60*dias) + (0.15*km))
    
    linha60()
    print(f'O custo total por {dias} dias e {km:.2f} km rodados é de R$ {p:.2f}.')
    linha60()
