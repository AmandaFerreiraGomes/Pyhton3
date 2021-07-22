""" Desafio 042: """
# Programa Principal:


def main():
	a = int(input('Digite o valor do cateto: '))
	b = int(input('Digite o valor do outro cateto: '))
	c = int(input('Digite o valor de outro cateto: '))
	if (abs(b-c) < a < b + c) and (abs(a-c) < b < a + c) and (abs(a - b) < c < a + b):
		print(f'Os segmentos {a}, {b} e {c} podem formar um TRIÂNGULO!')
		if a == b and b == c:
			print('Triângulo Equilátero.')
		elif a != b and b != c and a != c:
			print('Triângulo Escaleno.')
		else:
			print('Triângulo Isósceles.')
	else:
		print('Os segmentos não podem formar um TRIÂNGULO!')
	
	
main()
