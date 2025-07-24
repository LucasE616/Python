# Desafio: Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50 por km em viagens de até 200km, e R$0,45 para viagens mais longas

distancia = int(input('Digite a distância em km de sua viagem: '))
preco200 = distancia * 0.50
precolonge = distancia * 0.45

if distancia <= 200:
    print('Sua passagem custará R${:.2f}'.format(preco200))
else:
    print('Sua passagem custará R${:.2f}'.format(precolonge))
