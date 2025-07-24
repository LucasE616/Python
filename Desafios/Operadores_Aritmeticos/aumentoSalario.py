# Desafio: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento

salario = float(input('Qual seu salário? '))

newSalario = salario + (salario * 0.15)

print('Seu salário atual é de R${:.2f}, mas com aumento de 15%, você receberá R${:.2f}'.format(salario, newSalario))