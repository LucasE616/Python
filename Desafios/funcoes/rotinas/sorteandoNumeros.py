# Desafio: Faça um programa que tenha uma lista chamada NUMEROS e duas funções chamadas sorteio() e somaPar(). A primeira função vai 5 numertos e colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os pares sorteados pela função anterior.

from random import randint
from time import sleep

numeros = []

def sorteio():
    print('=' * 25)
    print('Sorteando números...')
    print('-' * 20)
    sleep(.5)
    for c in range(0, 5):
        numeros.append(randint(0, 100))
        print(numeros[c], end=' ')
        sleep(.5)
    print()
    print('=' * 25)
    print()


def somaPar(lista):
    print('=' * 25)
    print('Somando números pares...')
    print('-' * 26)
    sleep(.5)
    soma = 0
    for c in range(0, len(lista)):
        if lista[c] % 2 == 0:
            soma += lista[c]
            print(f'Somando {lista[c]}')
            sleep(.5)
    print(f'A soma dos valores pares da lista {numeros} é igual a {soma}')
    print('=' * 75)
    print()


sorteio()
somaPar(numeros)
