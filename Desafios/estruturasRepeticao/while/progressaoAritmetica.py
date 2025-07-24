# Desafio 1: Desenvolva um programa que leia o primeiro termo de uma Progressao Aritmética e a razão de um número. No final, mostre os 10 primeiros termos dessa PA.

primeiroTermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razao da PA: '))
decimoTermo = primeiroTermo + (10 - 1) * razao


# Solução encontrada em pesquisa:
termo = primeiroTermo
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('Fim! \n')

# Minha solução
while primeiroTermo <= decimoTermo:
    print(primeiroTermo, end='  ')
    primeiroTermo += razao


print('Fim!')
