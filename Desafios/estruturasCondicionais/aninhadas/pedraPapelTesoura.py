# Desafio: Crie um jogo que faça o PC jogar Pedra Papel Tesoura com você

from random import randint

print('''Sua opções: 
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
jogador = int(input('Qual a sua jogada? '))

print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))

if computador == 0: # PC joga Pedra
    if jogador == 0: # Pedra
        print('Empate!')
    elif jogador == 1: # Papel
        print('Jogador ganhou!')
    elif jogador == 2: # Tesoura
        print('Computador ganhou!')
    else:
        print('Jogada inválida!')
elif computador == 1: # PC joga Papel
    if jogador == 0: # Pedra
        print('Computador ganhou!')
    elif jogador == 1: # Papel
        print('Empate!')
    elif jogador == 2: # Tesoura
        print('Jogador ganhou!')
    else:
        print('Jogada inválida!')
elif computador == 2: # PC joga Tesoura
    if jogador == 0: # Pedra
        print('Jogador ganhou!')
    elif jogador == 1: # Papel
        print('Computador ganhou!')
    elif jogador == 2: # Tesoura
        print('Empate!')
    else:
        print('Jogada inválida!')
