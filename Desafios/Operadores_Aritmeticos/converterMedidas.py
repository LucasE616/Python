# Desafio: Escreva um programa que leia um valor em metros e o exiba em centímetros

metro = float(input('Digite sua altura em metros: '))

centimetro = metro * 100
milimetro = metro * 1000

print('Sua altura é {} metros. \n Sua altura em centímetros é {:.0f}cm. Sua altura em milímetros é {:.0f}mm'.format(metro, centimetro, milimetro))