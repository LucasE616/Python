# Desafio: Escreva um programa que pergunte o salário de uma pessoa e calcule o seu aumento.
    # Para salário acima de R$1250,00, calcule um aumento de 10%
    # Para salário abaixo disso, calcule um aumento de 15%

salario = int(input('Digite o salario: '))
salario10 = salario + salario * 0.10
salario15 = salario + salario * 0.15


if salario >= 1250:
    print('Seu novo salário é de R${:.2f}'.format(salario10))
else:
    print('Seu novo salário é de R${:.2f}'.format(salario15))
