# Desafio: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final mostre os valores pares e ímpares em ordem crescente.

numeros = [[], []]

for c in range(0, 7):
    num = int(input(f'Digite o {c+1}° número: '))
    if num % 2 == 0:
        numeros[0].append(num)
    elif num % 2 == 1:
        numeros[1].append(num)

numeros[0].sort()
numeros[1].sort()
print(f'Os números pares digitados foram: {numeros[0]} \n Os números impares digitados foram: {numeros[1]}')
