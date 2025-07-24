# Desafio: Crie um programa onde 5 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vendedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter

jogoDado = {
    'jogador01': randint(1, 6),
    'jogador02': randint(1, 6),
    'jogador03': randint(1, 6),
    'jogador04': randint(1, 6),
    'jogador05': randint(1, 6)
}

ranking = []

for j, n in jogoDado.items():
    print(f'O jogador {j} tirou o número {n} no dado...')
    sleep(.5)

print(f'\n {'-_' * 25} \n')

print(f'Ranking dos jogadores:')
ranking = sorted(jogoDado.items(), key=itemgetter(1), reverse=True) # itemgetter na posição 1, ordena pelo número sorteado. Na posição 0, ordena pelo número do jogador.
for i ,v in enumerate(ranking):
    print(f'{i+1}º lugar = {v[0]} com {v[1]} pontos')
    sleep(.5)
