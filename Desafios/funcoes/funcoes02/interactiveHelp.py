# Desafio: Faça um mini programa que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra "FIM", o programa se encerrará. OBS: Use as cores

c = ('\033[m',        # 0 - Sem cores;
     '\033[0;30;41m', # 1 - Vermelho;
     '\033[0;30;42m', # 2 - Verde;
     '\033[0;30;43m', # 3 - Amarelo;
     '\033[0;30;44m', # 4 - Azul;
     '\033[0;30;45m', # 5 - Roxo;
     '\033[7m'        # 6 - Branco.
     )

# Função principal
def ajuda(cmd):
    titulo(f'Acessando o manual do comando \'{cmd}\'', 4)
    print(c[6], end='')
    help(cmd)
    print(c[0], end='')


# Função do título, apenas
def titulo(msg, cor=0):
    tamanho = len(msg) + 4
    print(c[cor], end='')
    print('-' * tamanho)
    print(f'  {msg}')
    print('-' * tamanho)
    print(c[0], end='')


# Programa principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou biblioteca: '))
    if comando.upper().strip() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Até logo...', 1)
