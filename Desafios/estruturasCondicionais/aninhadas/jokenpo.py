# Desafio: Crie um jogo que faça o PC jogar Jokenpô com você

from random import randint

jogaPC = randint(1,3)
player = int(input('Faça sua escolha: \n 1 - Pedra \n 2 - Papel \n 3 - Tesoura \n \n Digite sua escolha: '))

print('Você escolheu {}, o PC escolheu {}'.format(player, jogaPC))

if player == jogaPC:
    print('Empate!')
elif jogaPC == 1 and player == 2:
    print('Você ganhou!')
elif jogaPC == 1 and player == 3:
    print('O PC ganhou!')
elif player == 1 and jogaPC == 2:
    print('O PC ganhou!')
elif player == 1 and jogaPC == 3:
    print('Você ganhou!')
else:
    print('Jogada inválida!')
