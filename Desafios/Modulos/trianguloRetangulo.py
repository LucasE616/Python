# Desafio: Faca um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo e calcule o comprimento da hipotenusa
# formula: hipotenusa² = catetoOposto² + catetoAdjacente²

from math import sqrt, pow, hypot

catetoOposto = int(input('Digite o valor do Cateto Oposto: '))
catetoAdjacente = int(input('Digite o valor do Cateto Adjacente: '))
hipotenusa = sqrt(pow(catetoOposto, 2) + pow(catetoAdjacente, 2))

# Outra maneira mais fácil de calcular o valor da hipotenusa é usando a importação hypot
importHipotenusa = hypot(catetoOposto, catetoAdjacente)

print('Cateto Oposto: {} \n Cateto Adjacente: {} \n O valor da Hipotenusa é: {}. \n Usando o hypot: {}'.format(catetoOposto, catetoAdjacente, hipotenusa, importHipotenusa))
