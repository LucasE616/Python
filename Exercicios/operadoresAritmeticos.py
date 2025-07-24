n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2
divInt = n1 // n2
resto = n1 % n2
exp = n1 ** n2

print('Você digitou os números {} e {}. \n E os resultados das operações usando eles estão abaixo:'.format(n1, n2))  # O comando \n serve para quebrar a linha dentro do terminal
print('A soma de {} + {} = {}'.format(n1, n2, soma))
print('A subtração de {} - {} = {}'.format(n1, n2, sub))
print('A multiplicação de {} x {} = {}'.format(n1, n2, mult))
print('A divisão de {} / {} = {}'.format(n1, n2, div))
print('A divisão inteira de {} // {} = {}. '.format(n1, n2, divInt), end='')  # O comando end='' serve para não quebrar a linha dentro do terminal
print('E o resto da divisão de {} % {} = {}'.format(n1, n2, resto))
print('A exponenciação de {} ** {} = {}'.format(n1, n2, exp))
