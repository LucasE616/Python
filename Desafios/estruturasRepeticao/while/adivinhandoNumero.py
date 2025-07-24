# Desafio: Crie um programa onde o PC vai pensar um número entre 0 e 25, o jogador vai jogar até acertar, mostrando a quantidade de tentativas necessárias para vencer.

from random import randint

numPC = randint(0, 25)
numUser = int(input('Digite um número entre 0 e 25: '))
tentativas = 1

while numUser != numPC:
    if numUser > numPC:
        numUser = int(input('Você errou! Tente um número menor... \n Digite outro número entre 0 e 25: '))
    if numUser < numPC:
        numUser = int(input('Você errou! Tente um número maior... \n Digite outro número entre 0 e 25: '))

    tentativas += 1

print('Parabéns, você acertou em {} tentativas!'.format(tentativas))
