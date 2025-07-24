# Desafio: Faça um programa que mostre a tabuada de um número escolhido pelo usuário

num = int(input('Digite um número: '))

for c in range(0, 11):
    print('{} x {} = {}'.format(num, c, num * c))
print('FIM')
