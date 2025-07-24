# Desafio: Crie um programa que leia dois valores e mostre um menu na tela:
    # [1] Somar
    # [2] Multiplicar
    # [3] Maior
    # [4] Novos valores
    # [5] Sair do programa
# Realize a operação solicitada em cada caso

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
opt = int(input('Escolha a ação que deseja realizar: \n [1] - Somar \n [2] - Multiplicar \n [3] - Maior valor \n [4] - Novos valores \n [5] - Sair do programa \n Digite: '))

while opt != 5:
    if opt == 1:
        soma = num1 + num2
        print('A soma dos números {} + {} = {}'.format(num1, num2, soma))
        opt = 5
    elif opt == 2:
        multiplicacao = num1 * num2
        print('A multiplicação dos números {} x {} = {}'.format(num1, num2, multiplicacao))
        opt = 5
    elif opt == 3:
        if num1 > num2:
            print('{}, primeiro número escolhido é o maior.'.format(num1))
        elif num2 > num1:
            print('{}, segundo número escolhido é o maior.'.format(num2))
        else:
            print('Os números {} e {} são iguais!'.format(num1, num2))
        opt = 5
    elif opt == 4:
        print('Escolha novos valores: ')
        num1 = int(input('Digite o primeiro valor: '))
        num2 = int(input('Digite o segundo valor: '))
        opt = int(input('Escolha a ação que deseja realizar: \n [1] - Somar \n [2] - Multiplicar \n [3] - Maior \n [4] - Novos valores \n [5] - Sair do programa \n Digite: '))
    else:
        print('Você digitou uma opção inválida!')
        opt = int(input('Digite uma opção: \n [5] - Sair do programa \n [6] - Voltar para o programa \n Digite: '))
        if opt == 6:
            num1 = int(input('Digite o primeiro valor: '))
            num2 = int(input('Digite o segundo valor: '))
            opt = int(input('Escolha a ação que deseja realizar: \n [1] - Somar \n [2] - Multiplicar \n [3] - Maior \n [4] - Novos valores \n [5] - Sair do programa \n Digite: '))
print('Fim!')
