# Desafio: Faça um algoritmo que leia preço de um produto e mostre seu novo preço com 5% de desconto

precoInicial = float(input('Qual o preço do seu produto? '))

desconto = precoInicial - (precoInicial * 0.05)

print('O preço do seu produto é de R${:.2f}, com 5% de desconto fica R${:.2f}'.format(precoInicial, desconto))