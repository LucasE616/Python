# Crie um programa que simula um caixa eletrônico. O usuário começa com um saldo fictício de R$ 1000,00.
    # O programa apresenta um menu com as opções:
        # [1] Ver saldo
        # [2] Sacar dinheiro
        # [3] Depositar dinheiro
        # [4] Sair
    # O programa deve continuar exibindo o menu até que o usuário escolha a opção de sair (4), usando um laço while.
        # Regras:
            # Para saque, verifique se há saldo suficiente.
            # Para depósito, só aceite valores positivos.
            # Exiba mensagens apropriadas para cada operação.

saldo = 1000
opt = int(input('Escolha uma opção: \n [1] - Ver saldo \n [2] - Sacar dinheiro \n [3] - Depositar dinheiro \n [4] - Sair \n Digite a opção: '))

while opt != 4:
    if opt == 1:
        print('\n Seu saldo é: R${:.2f} '.format(saldo))
    elif opt == 2:
        saque = float(input('\n Qual valor deseja sacar? R$: '))
        if saque > saldo:
            print('\n Saldo insuficiente. Seu saldo é: R${:.2f}'.format(saldo))
        else:
            saldo -= saque
            print('\n Você sacou R${:.2f}, seu novo saldo é: R${:.2f}'.format(saque, saldo))
    elif opt == 3:
        deposito = float(input('\n Qual valor deseja depositar? R$: '))
        saldo += deposito
        print('\n Você depositou R${:.2f}. Seu saldo é: R${:.2f} '.format(deposito, saldo))
    else:
        print('\n Opção inválida. Digite outra opção.')
    opt = int(input('\n Escolha uma opção: \n [1] - Ver saldo \n [2] - Sacar dinheiro \n [3] - Depositar dinheiro \n [4] - Sair \n Digite a opção: '))
print('Fim do programa!')
