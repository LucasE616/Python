# Desafio: Crie um programa que jogue par ou ímpar com o PC. O jogo seeá interrompido quando o jogador perder, mostrando o número de vitórias do usuário.

from random import randint

cont = 0

while True:
    numPC = randint(1, 2)
    num = int(input('Digite um número: '))
    parImpar = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    result = (num + numPC) % 2

    while parImpar not in 'PI':
        parImpar = str(input('Resposta inválida, tente novamente... \n Par ou Ímpar? [P/I] ')).strip().upper()[0]

    if parImpar == 'P':
        if result == 0:
            print(f'Você jogou {num}, o PC jogou {numPC}. \n Você ganhou!')
            cont += 1
        else:
            print(f'Você jogou {num}, o PC jogou {numPC}. \n Você perdeu!')
            break
    elif parImpar == 'I':
        if result == 1:
            print(f'Você jogou {num}, o PC jogou {numPC}. \n Você ganhou!')
            cont += 1
        else:
            print(f'Você jogou {num}, o PC jogou {numPC}. \n Você perdeu!')
            break
print(f'GAME OVER!!! \n Você ganhou {cont} vezes seguidas.')
print('Fim!')
