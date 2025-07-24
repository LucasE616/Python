# Desafio: Faça um desafio que ajude um jogador da Mega Sena a criar palpites. O programa vai perguntar quantos jogos serão geradose vai sortear 6 números entre 1 e 60 para para cada jogo, cadastrando em uma lista composta.

from random import randint

megaSena = []
jogos = []
quantJogos = int(input('Digite a quantidade de jogos que deseja fazer: '))

for c in range(quantJogos):
    for c in range(0, 6):
        r = randint(1, 61)
        if r in jogos:
            c -= 1
        elif r not in jogos:
            jogos.append(r)
    megaSena.append(jogos[:])
    jogos.clear()

for c, j in enumerate(megaSena):
    print(f'{c+1}° jogo: {j}')
