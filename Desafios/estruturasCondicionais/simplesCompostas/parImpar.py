# Desafio: Crie um programa que diga se um número é ímpar ou par

from random import randint

numero = randint(0, 1000)

if numero % 2 == 0:
    print('Número {} é par.'.format(numero))
else:
    print('Número {} é ímpar.'.format(numero))
