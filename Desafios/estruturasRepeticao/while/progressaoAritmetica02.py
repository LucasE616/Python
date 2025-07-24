# Desafio 1: Desenvolva um programa que leia o primeiro termo de uma Progressao Aritmética e a razão de um número. No final, mostre os 10 primeiros termos dessa PA.
# Desagio 2: Pergunte se o usuários quer mais termos da PA, caso escolha 0 termos, o programa se encerra.

primeiroTermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razao da PA: '))
decimoTermo = primeiroTermo + (10 - 1) * razao
termo = primeiroTermo
cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos a mais você quer mostrar? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
