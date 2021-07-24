""" Desafio 011: """


def linha():
	  print('-' * 40)


def area_retangulo(b, h):
  	area = b * h
	  return area


if __name__ == "__main__":
    linha()
    print("     QUANTIDADE DE TINTA NECESSÁRIA     ")
    linha()
   
    # entrada de dados para a área e para a base:
    h = float(input('Altura(m): '))  # o usuário insere a medida da altura, que é um número real.
    b = float(input('Largura(m): '))  # o usuário insere a medida da base, que, também, é um número real.
    linha()

    # a variável a recebe
    a = area_retangulo(b, h)

    # quatidade de tinta necessária:
    qtd_tinta = (a / 2)

    # exibição do resultado:
    print(f'Para pintar uma área de {a:.1f} m² serão necessários {qtd_tinta:.1f} litros de tinta.')
