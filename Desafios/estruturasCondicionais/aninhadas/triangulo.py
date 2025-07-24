# Desafio: Desenvolva um programa que leia o comprimento de três retas e diga se podem ou não formar um triângulo
    # Para saber se é possível formar o triangulo, é preciso verificar se a soma de dois lados é maior que o terceiro lado
        # A + B > C
        # A + C > B
        # B + C > A
    # Mostre o tipo de triângulo que será formado:
        # Equilátero: Todos os lados iguais;
        # Isósceles: Dois lados iguais;
        # Escaleno: Todos os lados diferentes.

print('Digite os valores das retas para saber se formam um triângulo.')
reta1 = int(input('Reta 1: '))
reta2 = int(input('Reta 2: '))
reta3 = int(input('Reta 3: '))

if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print('As três retas são capazes de formar um triângulo.')
    if reta1 == reta2 == reta3:
        print('É um triângulo Equilátero.')
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print('É um triângulo Isósceles.')
    else:
        print('É um triângulo Escaleno')
else:
    print('As três retas não são capazes de formar um triângulo.')
