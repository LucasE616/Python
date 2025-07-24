# Desafio: Faça um programa que leia um número de 0 a 9999 e mostre cada um dos dígitos separados. Ex: 1834, unidade: 4, dezena: 3, centena: 8, milhar: 1

from random import randint

numero = randint(0, 9999)
lerNumero = str(numero)
unidade = numero // 1 % 10
dezena  = numero // 10 % 10
centena = numero // 100 % 10
milhar  = numero // 1000 % 10

print('O número sorteado foi {}'.format(numero))
print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))
