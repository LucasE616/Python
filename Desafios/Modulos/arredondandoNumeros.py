# Desafio: Leia um número real e arredonde ele para um número inteiro
from math import floor, ceil, trunc

numero = float(input('Digite um número real: '))

cortaInt = trunc(numero)
arredondadoBaixo = floor(numero)
arredondadoCima = ceil(numero)
# Usando a tag int(), também é possível extrair a parte inteira de um número real

print('O número digitado foi {}. \nCortando a parte inteira, fica assim: {}. \n Ele arredondado para baixo é: {}. \n Já o número arredondado para cima é {}.'.format(numero, cortaInt, arredondadoBaixo, arredondadoCima))
