# Escreva um programa que faça o PC "pensar" um número inteiro entre 0 e 5 e peça o usuário para tentar descobrir o número escolhido pelo PC.

from random import randint
from time import sleep

numSorteado = randint(0, 5)
numUser = int(input('Digite um número de 1 a 5: '))

print('Sorteando...')
sleep(1)

if numUser == numSorteado:
    print('Você acertou!')
else:
    print('Você errou! O número sorteado foi {}'.format(numSorteado))
