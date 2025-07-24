# Desafio: Desenvolva um programa que leia seis números inteiros e mostre a soma dos números pares. Se for ímpar, desconsidere...

soma = 0
cont = 0

for c in range(1, 7):
    cont = int(input('Digite {}º valor: '.format(c)))
    if cont % 2 == 0:
        cont += 1
        soma += cont
print('A soma de {} números pares é {}'.format(cont, soma))
print('FIM')
