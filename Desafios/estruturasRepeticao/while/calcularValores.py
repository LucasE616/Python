# Desafio: Crie um programa que leia vários números inteiros pelo teclado. O programa vai parar quando o valor 999 for digitado. No final, mostre quantos números foram digitados e a soma entre eles(desconsiderando o 999).

num = int(input('Digite um número [Digite 999 para encerrar o programa]: '))
cont = 0
soma = 0

while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite o {}° número [Digite 999 para encerrar o programa]: '.format(cont + 1)))
print('Você digitou {} valores. E a soma entre eles é: {}'.format(cont, soma))
