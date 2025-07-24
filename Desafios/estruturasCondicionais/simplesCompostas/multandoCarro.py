# Desafio: Escreva um programa que leia a velocidade de um carro.
    # Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
    # A multa vai custar R$7,00 para cada km/h acima do limite.

velocidade = int(input('Digite a velocidade em Km/h: '))
multa = (velocidade - 80) * 7

if velocidade > 80:
    print('Você estava dirigindo à {}km/h, acima do limite de velocidade permitido. \n Você irá receber uma multa de R${},00.'.format(velocidade, multa))
if velocidade < 40:
    print('Você está abaixo do limite permitido, acelere para uma velocidade entre 40km/h e 80km/h.')
else:
    print('Você estava dirigindo à {}km/h, dentro do limite de velocidade permitido e se livrou da multa.'.format(velocidade))
