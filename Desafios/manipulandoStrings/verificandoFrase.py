# Desafio: Faça um programa que leia uma frase e mostre:
    # Quantas vezes a letra 'A' aparece;
    # Em que posição ela aparece a primeira vez;
    # Em que posição ela aparece a útima vez.

digiteFrase = 'Lorem ipsum cubilia mollis viverra pulvinar, tincidunt sapien commodo cursus iaculis, mauris quisque nisi justo.'
frase = digiteFrase.upper().strip()

print('A letra A aparece {} vezes.'.format(frase.count('A')))
print('A letra A aperece a primeira vez na posição {}.'.format(frase.find('A')))
print('A letra A aparece a última vez na posição {}.'.format(frase.rfind('A')))