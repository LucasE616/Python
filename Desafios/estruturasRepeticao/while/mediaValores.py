# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar se o usuário quer ou não continuar a digitar.

resposta = 'S'
soma = quant = media = maior = menor = 0

while resposta in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1

    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
media += num / quant
print('Você digitou {} números. A média entre eles é {} \n O maior número é {}. O menor número é {}'.format(quant, media, maior, menor))
