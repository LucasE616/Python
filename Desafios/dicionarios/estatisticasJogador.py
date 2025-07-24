# Desafio 02: Aprimore o desafio dadosJogador, para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogador = {}
time = []
partidas = []

# Capturar dados dos jogadores
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    totalJogos = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, totalJogos):
        partidas.append(int(input(f'Quantas gols na partida {c+1}: ')))
    jogador['partidas'] = partidas[:]
    jogador['totalGols'] = sum(partidas)
    time.append(jogador.copy())

    while True:
        continua = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if continua in 'SN':
            break
        print(f'ERROR!!! \n Responda apenas Sim ou Não')
    if continua == 'N':
        break

print('-='*25)
# Mostrar cabeçalho
print(f'COD ' , end=' ')
for i in jogador.keys():
    print(f'{i:<15}' , end='')
print()

# Mostrar dados dos usuários
for k, v in enumerate(time):
    print(f'{k:>3} ', end=' ') # Mostrar índices ( o, 1, 2, 3...)
    for d in v.values():
        print(f'{str(d):<15}', end=' ') # Mostrar valores dos dados
    print()
print('-='*25)

# Verificar quais dados individuais mostrar
while True:
    busca = int(input(f'Qual jogador deseja buscar? (999 para encerrar!)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Não existe jogador com o código {busca}! \n TENTE NOVAMENTE')
    else:
        print(f'-> Dados detalhados do jogador {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]["partidas"]):
            print(f' --> No jogo {i+1} fez {g} Gols')
print('--- PROGRAMA ENCERRADO ---')
