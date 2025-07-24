# Desafio: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo, e realize a contagem.
    # O programa tem que realizar três contagens através da função criada:
        # De 1 até 10, de 1 em 1;
        # De 10 até 0, de 2 em 2;
        # Uma contagem personalizada.

from time import sleep

def contador(inicio, fim, passo):
    print('-_' * 25)
    if passo == 0:
        passo = 1
    if fim < inicio:
        print(f'Contagem de {inicio} até {passo}, de {abs(passo)} em {abs(passo)}:')
        for c in range(inicio, fim - 1, -abs(passo)):
            print(c, end=' ')
            sleep(.5)
        print('FIM!')
    else:
        print(f'Contagem de {inicio} até {fim}, de {abs(passo)} em {abs(passo)}:')
        for c in range(inicio, fim + 1, abs(passo)):
            print(c, end=' ')
            sleep(.5)
        print('FIM!')
    print('-_' * 25)
# OBS: A função abs() faz com que o valor seja absoluto, exemplo: digita -1, saída 1
# Também é possível multiplicar o valor negativo por -1, exemplo: valor *= -1


contador(1, 10, 1)
contador(10, 0, 2)
print('-_' * 25)
print(f'Agora personalize sua contagem...')
sleep(.75)
inicioCont = int(input('Inicio: '))
fimCont = int(input('Fim: '))
passoCont = int(input('Passo: '))
contador(inicioCont, fimCont, passoCont)
