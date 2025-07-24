# Desafio: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno e cosseno desse ângulo

from math import sin, cos, radians

grau = int(input('Digite um ângulo em graus: '))

anguloRadianos = radians(grau)

seno = sin(anguloRadianos)
cosseno = cos(anguloRadianos)

print('O ângulo {}, em graus radianos é {:.2f}. \n O seu seno é {:.2f}, já seu cosseno é {:.2f}'.format(grau, anguloRadianos, seno, cosseno))