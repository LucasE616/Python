# Desafio: Faça um programa que tenha uma função chamada area(), que receba as dimensões de um terreno retangular(largura e comprimento)e mostre a área do terreno.

def area(largura, comprimento):
    areaTerreno = largura * comprimento
    print(f'A área do terreno que possui {largura:.2f}mx{comprimento:.2f}m é de {areaTerreno:.2f}m²')


print(f'Controle de Terrenos:')
print('-' * 25)
larguraTerreno = float(input('Largura do terreno(m): '))
comprimentoTerreno = float(input('Comprimento do terreno(m): '))

area(larguraTerreno, comprimentoTerreno)
