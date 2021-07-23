""" Desafio 008: """


def linha():
    print('-'*25)


if __name__ == '__main__':
  
    n = float(input('Digite o valor em metros: '))
    
    # Casos em que deseja-se transformar de um maior (metro) para um menor (cm, mm, dm). *Por isso usa-se a multiplicação.
    m_cm = n * 100 # conversão de metros para centímetros. 1 metro -> 100 centímetros.
    m_mm = n * 1000 # conversão de metros para milímetros. 1 metro -> 1000 milímetros.
    m_dm = n * 10 # conversão de metros para decímetros. 1 metro -> 100 decímetros.
    
    # Casos em que deseja-se transformar de um menor (metro) para um maior (cm, mm, dm). *Por isso usa-se a divisão.
    m_dam = n / 10 # conversão de metros para decâmetros. 10 metros -> 1 decâmetros.
    m_hm = n / 100 # conversão de metros para hectômetro. 100 metros -> 1 hectômetro.
    m_km = n / 1000 # conversão de metros para quilômetros. 1000 metros -> 1 quilômetro.
    
    linha()
    print('\t	CONVERSÃO')
    linha()
    
    print('{} m -> {} cm \n{} m -> {} mm\n{} m -> {} dm'.format(n, m_cm, n, m_mm, n, m_dm))
    print('{} m -> {} dam\n{} m -> {} hm\n{} m -> {} km.'.format(n, m_dam, n, m_hm, n, m_km))
