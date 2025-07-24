# Desafio: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade

from datetime import date

ano = date.today().year
contadorMaior = 0
contadorMenor = 0

for c in range(1, 8):
    nascimento = int(input('Digite seu ano de nascimento: '))
    idade = ano - nascimento
    if idade >= 18:
        contadorMaior += 1
    else:
        contadorMenor += 1
print('{} pessoas são maiores de idade.'.format(contadorMaior))
print('{} pessoas são menores de idade.'.format(contadorMenor))