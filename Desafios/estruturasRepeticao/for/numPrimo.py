# Desafio: Crie um programa que leia um número inteiro e diga se ele é ou não um número primo

num = int(input('Digite um número: '))
total = 0

print('Para um número ser considerado NÚMERO PRIMO, ele deve ser divido apenas por 1 e por ele mesmo.')

for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n \033[m O número {} foi dividido por {} números'.format(num, total))

if total == 2:
    print('Por esse motivo, ele é primo.')
else:
    print('Por esse motivo, ele não é primo.')
