# Desafio: Desenvolva um programa que leia o nome, idade e sexo de 5 pessoas. No final mostre:
    # A média de idade do grupo;
    # Qual é o homem mais velho;
    # Quantas mulheres tem menos de 20 anos

mediaIdade = 0
mulheres20 = 0
idadeHomem = 0
homemVelho = 'Alguém'

for c in range(1, 6):
    print('{}° Pessoa: '.format(c))
    nome = str(input('Digite seu nome: ')).strip()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo (M/F): ')).upper().strip()
    print(' ')

    mediaIdade += idade

    if sexo == 'M':
        if idade > idadeHomem:
            idadeHomem = idade
            homemVelho = nome
    elif sexo == 'F':
        if idade < 20:
            mulheres20 += 1
    else:
        print('Sexo inválido.')

print('A média de idade do grupo é de {}'.format(mediaIdade / 5))
print('O homem mais velho é o {}'.format(homemVelho))
print('Tem {} mulheres com menos de 20 anos'.format(mulheres20))
