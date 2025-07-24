# Desafio: Faça um programa que leia 3 números e diga qual é o maior e qual é o menor

from random import randint

numero1 = randint(1, 10)
numero2 = randint(1, 10)
numero3 = randint(1, 10)

print('Numeros sorteados: \n Número 1: {} \n Número 2: {} \n Número 3: {}'.format(numero1, numero2, numero3))

maiorNumero = numero1
menorNumero = numero1

if maiorNumero < numero2:
    maiorNumero = numero2
if maiorNumero < numero3:
    maiorNumero = numero3
print('O maior número é: {}'.format(maiorNumero))

if menorNumero > numero2:
    menorNumero = numero2
if menorNumero > numero3:
    menorNumero = numero3
print('O menor número é: {}'.format(menorNumero))
