# Desafio: Crie um programa que leia o fatorial de um número.

from math import factorial

num = int(input('Digite um valor: '))
fatorial = 1

# Solução encontrada em pesquisa:
cont = num
print('Calculando {}! = '.format(num), end='')
while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    cont -= 1
print('{} \n'.format(factorial(num)))

# Minha solução:
while num > 1:
    fatorial *= num
    num = num - 1
    print('{} x {} = {}'.format(fatorial, num, fatorial * num))
print('O Fatorial do número escolhido é {}'.format(fatorial))
