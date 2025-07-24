# Desafio: Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de Fibonacci
    # Fórmula: F(n) = F(n-1) + F(n-2)

num = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('{} -> {}'.format(t1, t2), end='')
contador = 3 # o contador começa em 3 por que o primeiro e o segundo termos já foram mostrados acima

while contador <= num:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    contador += 1
print(' -> FIM')
