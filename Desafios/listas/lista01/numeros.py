# Desafio: Faça um programa que leia 5 valores numéricos pelo teclado e guarde-os em uma lista. No final, mostre qual foi o maior e o menos número digitado e as suas respectivas posições na lista.

num = []
ordem = []
menor = maior = 0

for c in range(0, 5):
    num.append(int(input(f'Digite o valor da posição {c}: ')))
print(num)
ordem = sorted(num)

print(ordem)

print(f'O menor valor é {ordem[0]}. E está na posição ', end='')
for i, valor in enumerate(num):
    if valor == ordem[0]:
        print(f"{i}...", end=' ')

print(f'\n O maior valor é {ordem[-1]}. E está na posição ', end='')
for i, valor in enumerate(num):
    if valor == ordem[-1]:
        print(f"{i}...", end=' ')
