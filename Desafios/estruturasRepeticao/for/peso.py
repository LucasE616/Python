# Desafio: Faça um programa que leia o peso de cinco pessoas. No fim, mostre qual o maior e o menos peso lidos.

maior = 0
menor = 0

for c in range(1, 6):
    peso = float(input('Digite o peso da {}° pessoa em Kg: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido é: {}Kg. \n O menor peso lido é: {}Kg.'.format(maior, menor))
