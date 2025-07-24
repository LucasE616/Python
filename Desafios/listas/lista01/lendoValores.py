# Desafio: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-se em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, os valores serão exibidos em ordem crescente.

continua = 'S'
num = []

while continua == 'S':
    num.append(int(input('Digite um valor: ')))
    # Também dá para usar uma variável para ler os valores, e usar um IF VALOR DIGITADO NOT IN NUM[]
    if len(num) != len(set(num)): # set serve para remover duplicatas
        print(f'Número digitado já existe na lista e não pode ser inserido')
        num.pop()
    continua = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    while continua not in 'SN':
        continua = str(input('Opção incorreta! \n Deseja continuar? [S/N]')).strip().upper()[0]
    if continua == 'N':
        print(num)
        print(sorted(num))
        break
