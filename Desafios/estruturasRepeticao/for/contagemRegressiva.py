# Desafio: Faça um programa que mostre na tela uma contagem regressiva, indo de 10 até 0, com pausa de 1 segundo

from time import sleep

for i in range(10, -1, -1):
    print(i)
    sleep(1)
print('FIM')