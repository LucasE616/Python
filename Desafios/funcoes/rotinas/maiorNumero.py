# Desafio: Faça um programa que tenha uma função chamada maior(), que receba vários parâmeteros com valores inteiros. Seu programa qtem que analisar todos os valores e dizer qual deles é o maior.

from random import randint
from time import sleep

def maior(lista):
    print('-' * 20)
    print('Sorteando números...')
    print('-' * 20)
    if len(lista) == 0:
        print('Nenhum número sorteado...')
    else:
        maiorNumero = 0
        for c in range(0, len(lista)):
            print(f'{lista[c]}', end=' ')
            sleep(0.5)

            if c == 0:
                maiorNumero = lista[c]
            elif lista[c] > maiorNumero:
                maiorNumero = lista[c]
        print()
        print(f'O maior número da lista é: {maiorNumero}')
        print()


listaVazia = []
listaNum = []
for c in range(0, 10):
    listaNum.append(randint(0, 100))

maior(listaNum)
maior(listaVazia) # Testando validação de lista vazia
