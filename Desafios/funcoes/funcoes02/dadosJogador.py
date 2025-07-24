# Desafio: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
    # O nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(jogador='', gols=''):
    if jogador.strip() == '':
        jogador = '<desconhecido>'

    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    return f'O nome do jogador é {jogador} e ele marcou {gols} gols.'


nomeJogador = str(input('Nome do jogador: '))
numGols = str(input('Número de gols: '))

print(ficha(nomeJogador, numGols))
