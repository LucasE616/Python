# Desafio: Escreva um valor que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
    # O primeiro valor é maior
    # O segundo valor é maior
    # Os valores são iguais

numero1 = int(input('Digite o valor do primeiro número: '))
numero2 = int(input('Digite o valor do segundo número: '))

if numero1 > numero2:
    print('O valor do primeiro número é maior!')
elif numero1 < numero2:
    print('O valor do segundo número é maior!')
else:
    print('Os valores são iguais!')
