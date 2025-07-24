# Desafio: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F". Caso esteja errado peça novamente até ser digitado o valor correto.

sex = str(input('Qual seu sexo? [M/F] ')).strip().upper()[0]

while sex not in 'MF':
    sex = str(input('Dado inválido! \n Digite seu sexo novamente [M/F] ')).strip().upper()[0]
print('Fim!')
