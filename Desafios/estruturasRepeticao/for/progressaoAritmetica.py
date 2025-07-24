# Desafio: Desenvolva um programa que leia o primeiro termo de uma Progressao Aritmética e a razão de um número. No final, mostre os 10 primeiros termos dessa PA.

primeiroTermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razao da PA: '))
decimoTermo = primeiroTermo + (10 - 1) * razao

for c in range(primeiroTermo, decimoTermo + razao, razao):
    print(c)
print('FIM')