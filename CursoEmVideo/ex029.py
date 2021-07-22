""" Desafio 029: """
# Programa Pricipal:
print('-'*30)
v = float(input('Velocidade(km/h): '))
print('-'*30)
if v > 80:
	multa = (v-80)*7
	print(f'Você foi multado(a) em R$ {multa:.2f}.')
else:
	print('Parabéns! Você respeita as normas de trânsito!')
print('-'*30)
