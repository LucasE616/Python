# Desafio: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso mostre:
    # Quantos números foram digitados;
    # A lista de valores, ordenada de forma decrescente;
    # Se o valor 5 foi digitado e está na lista.

num = []

while True:
    num.append(int(input('Digite um valor: ')))

    continua = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    while continua not in 'SN':
        continua = str(input('Opção incorreta! \n Deseja continuar? [S/N]')).strip().upper()[0]
    if continua == 'N':
        break

print(f'Foram digitados {len(num)} números.')
print(f'A lista ordenada é: {sorted(num, reverse=True)}')
if 5 in num:
    print(f'O número 5 foi digitado na lista')
else:
    print(f'O número 5 não foi digitado na lista')
