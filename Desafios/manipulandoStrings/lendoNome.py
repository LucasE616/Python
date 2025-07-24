# Desafio: Crie um programa que leia o nome completo de uma pessoa e mostre:
    # 01 - O nome com todas as letras maiúsculas;
    # 02 - O nome com todas as letras minúsculas;
    # 03 - Quantas letras tem ao todo, sem considerar os espaços;
    # 04 - Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome: '))
palavra = nome.split() # Separando os nomes

print(nome.strip()) # O comando strip(), serve para remover espaços antes e depois do nome completo
print('O nome em letras maiúsculas é: {}'.format(nome.upper()))
print('O nome em letras minúsculas é: {}'.format(nome.lower()))
print('O nome tem {} letras.'.format(len(nome) - nome.count(' ')))
print('O primeiro nome tem {} letras'.format(len(palavra[0])))

# Outra maneira de contar qual o tamanho do primeiro nome:
    # print('O primeiro nome tem {} letras'.format(nome.find(' ')))