# Desafio: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar:
    # O valor da casa, o salário do comprador e em quantos anos ele vai pagar.
    # Calcule o valor da prestação mensal. Sabendo que ela não pode exceder 30% do salário ou o empréstimo será negado.
    # Condições opcionais: quantidade de anos limitada, valor da casa limitada com base no salário

valorCasa = int(input('Digite o valor da casa: '))
salario = int(input('Digite o salário: '))
prestacoes = int(input('Em quantos anos você pretende pagar o empréstimo? '))
valorPrestacoes = valorCasa / (prestacoes * 12)

if valorPrestacoes > salario * 0.3:
    print('Seu empréstimo foi negado, o valor das prestações excedem o limite de 30% do seu salário!')
else:
    (print('Seu empréstimo foi aprovado, você irá pagar um valor de R${:.2f} mensais.'.format(valorPrestacoes)))