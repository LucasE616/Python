# Desafio: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas, uma para receber apenas números pares, outra apenas para valores ímpares. No final mostre as três listas

num = []
pares = []
impares = []

while True:
    num.append(int(input('Digite um valor: ')))

    continua = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    while continua not in 'SN':
        continua = str(input('Opção incorreta! \n Deseja continuar? [S/N]')).strip().upper()[0]
    if continua == 'N':
        break

for i in range(len(num)):
    if num[i] % 2 == 0:
        pares.append(num[i])
    elif num[i] % 2 == 1:
        impares.append(num[i])

print(f'A lista completa é: {num}')
print(f'Os números pares digitados foram {pares}')
print(f'Os números ímpares digitados foram {impares}')
