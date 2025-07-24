# Desafio: Crie uma tupla com os 20 primeiros colocados do Brasileirão(em 27/05/25). Em seguida mostre:
    # Apenas os 5 primeiros colocados;
    # Os 4 últimos colocados;
    # Uma lista em ordem alfabética;
    # Em que posição está o time do Red Bull;
    # Em que posição está o Cruzeiro Esporte Clube.

tabela = ('Palmeiras', 'Flamengo', 'Cruzeiro', 'Red Bull Bragantino', 'Fluminense', 'Ceará', 'Bahia', 'Corinthians', 'Mirassol', 'Atlético-MG', 'Botafogo', 'Grêmio', 'São Paulo', 'Internacional', 'Vasco', 'Fortaleza', 'Vitória', 'Santos', 'Juventude', 'Sport')

print(f'Os 5 primeiros colocados são: {tabela[:5]}')
print(f'Os 4 últimos colocados são: {tabela[-4:]}')
print(f'A tabela em ordem alfabética é: {sorted(tabela)}')
print(f'O Red Bull Bragantino está na posição {tabela.index('Red Bull Bragantino') + 1}')
print(f'O CRUZEIRO ESPORTE CLUBE está posição {tabela.index('Cruzeiro') + 1}')
