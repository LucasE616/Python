# Desafio: Crie um programa que leia vários números inteiros e pare quando for digitado 999. No final mostre quantos números foram digitados e a soma deles

num = soma = cont = 0
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'Foram digitados {cont} números. E a soma deles é igual a {soma}')
