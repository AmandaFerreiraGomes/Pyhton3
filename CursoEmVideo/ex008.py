""" Desafio 008: """

n = float(input('Digite o valor em metros: '))
m_cm = n * 100
m_mm = n * 1000
m_dm = n * 10
m_dam = n / 10
m_hm = n / 100
m_km = n / 1000
print('-'*25)
print('\t	CONVERSÃO')
print('-'*25)
print('{} m -> {} cm \n{} m -> {} mm\n{} m -> {} dm'.format(n, m_cm, n, m_mm, n, m_dm))
print('{} m -> {} dam\n{} m -> {} hm\n{} m -> {} km.'.format(n, m_dam, n, m_hm, n, m_km))
