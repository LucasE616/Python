# Desafio: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o o usuário quer continuar.
    # No final mostre:
        # Quantidade de produtos;
        # Qual o total gasto na compra;
        # Quantos produtos custam mais de 1000 reias;
        # qual o produto mais barato.

cont = menor = mil = valor = 0
nomeMenor = 'Produto'

while True:
    produto = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: R$'))
    cont += 1
    valor += preco
    if preco >= 1000:
        mil += 1

    if cont == 1 or preco < menor:
        menor = preco
        nomeMenor = produto

    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Opção inválida, tente novamente... \n Deseja continuar? [S/N] '))
    if continuar == 'N':
        break
print(f'Total de produtos = {cont} \n Valor total da compra = R${valor:.2f} \n Produtos acima de 1000 reais = {mil} \n Produto mais barato = {nomeMenor} -> R${menor:.2f}')
