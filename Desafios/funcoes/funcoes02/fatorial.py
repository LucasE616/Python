# Desafio: Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
    # O primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico(opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial

def fatorial(numero, show=False):
    fat = 1
    for c in range(numero, 0, -1):
        fat *= c
        if show:
            if c > 1:
                print(f'{c} x', end=' ')
            elif c == 1:
                print(f'{c} =', end=' ')
    return fat


num = int(input('Digite o número que deseja calcular: '))
calc = str(input('Deseja exibir os cálculos? [S/N] ')).strip().upper()[0]
if calc == 'S':
    calc = True
elif calc == 'N':
    calc = False
print(fatorial(num, calc))
