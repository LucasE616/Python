# Desafio: Faça um programa que leia a largura e a altura de uma parede e calcule sua área e a quantidade de tinta necessária para pintá-la. Cada litro de tinta pinta 2m²

altura = float(input('Qual a altura(em metros) da parede que deseja pintar? '))
largura = float(input('E qual a largura(em metros) dessa parede? '))

areaParede = altura * largura

quantTinta = areaParede / 2

print('A sua parede de altura {}m e largura {}m, tem {}m² de área, e será necessário {} litros de tinta para pintá-la.'.format(altura, largura, areaParede, quantTinta))
