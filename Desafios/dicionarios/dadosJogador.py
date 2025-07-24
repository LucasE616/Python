# Desafio 01: Crie um programa que gerencie o aprovitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

from time import sleep

jogador = {}
partidas = []
jogador['nome'] = str(input('Nome do jogador: '))
totalJogos = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for c in range(0, totalJogos):
    partidas.append(int(input(f'Quantas gols na partida {c+1}: ')))
jogador['partidas'] = partidas[:]
jogador['totalGols'] = sum(partidas)

for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')

print('-='*25)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["partidas"])} partidas.')
print('-='*25)

for c, v in enumerate(jogador['partidas']):
    print(f' --> Na partida {c+1}: {v}')
    sleep(0.5)
print(f'{jogador["nome"]} fez um total de {jogador["totalGols"]} gols.')
