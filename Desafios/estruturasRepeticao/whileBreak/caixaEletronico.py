# Desafio: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte qual o valor a ser sacado(int) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS: Considere que o caixa possui cédulas de 50, 20, 10 e 1.

# Solução internet
valor = int(input('Digite o valor quer sacar: R$'))
total = valor
ced = 50
totCed = 0
while True:
    if total >= ced:
        total -= ced
        totCed += 1
    else:
        if totCed > 0:
            print(f'Total de {totCed} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totCed = 0
        if total == 0:
            break
print('Fim do programa!')

# Minha solução
num = int(input('Digite o valor que deseja sacar: R$'))
nota50 = num // 50
res20 = (num - (nota50 * 50)) // 20
nota10 = (num - (nota50 * 50) - (res20 * 20)) // 10
nota01 = (num - (nota50 * 50) - (res20 * 20) - (nota10 * 10)) // 1
print(f'50 = {nota50} \n 20 = {res20} \n 10 = {nota10} \n 01 = {nota01}')
