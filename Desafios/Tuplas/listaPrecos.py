# Desafio: Crie um programa que tenha uma única tupla com nomes de produtos e seus respectivos preços na sequência. No final, mostre uma listagem de preços,organizando os dados em forma tabular.

produtos = ('Teclado', 150, 'Mouse', 75, 'Monitor', 899, 'Notebook', 3200, 'Cadeira Gamer', 1200, 'Headset', 250, 'Impressora', 680, 'Webcam', 199, 'HD Externo', 350, 'Pen Drive', 45)

for c in range(0, len(produtos), 2):
    print(f'{produtos[c]:.<20}R${produtos[c+1]:.2f}')