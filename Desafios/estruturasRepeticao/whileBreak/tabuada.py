# Desafio: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido, quando for digitado um número negativo

while True:
    num = int(input('Digite um número (Digite um número negativo para encerrar o programa): '))
    if num < 0:
        break
    for c in range(0, 11):
        print(f'{num} x {c} = {num * c}')
print('Fim!')
