""" Desafio 017: """


# importando da biblioteca math a função sqrt(), a qual refere-se à raiz quadrada.
from math import sqrt


# Programa Principal: devolve a hipotenusa de um triângulo retângulo, cujos catetos oposto ao ângulo e adjacente ao ângulo são adicionados pelo usuário.
if __name__ == "__main__":
  
    # entrada dos valores dos catetos  
    co = float(input('Cateto oposto: '))
    ca = float(input('Cateto adjacente: '))
    
    # cálculo do valor da hipotenusa(h^2 = ca^2 + co^2 => h = (ca^2 + co^2)^1/2)
    h = sqrt(co**2 + ca**2)
    
    # exibição do resultado com precisão de uma casa decimal.
    print(f'A hipotenusa do Triângulo vale {h:.1f}.')
