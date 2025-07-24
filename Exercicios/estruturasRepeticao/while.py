# Lendo de 1 a 10

c = 1
while c <= 11:
    print(c)
    c += 1
print('Fim')
print('-' * 25)


# Enquanto o número ZERO não for digitado, continue o programa

n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('FIM')
print('-' * 25)


# Verificar se a pessoa quer continuar

r = 'S'
while r == 'S':
    n = int(input('Digite um número: '))
    r = str(input('Deseja continuar? [S/N] ')).strip().upper()
print('Fim!')
print('-' * 25)


# Par ou Ímpar

n = 1
par = impar = cont = 0

while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
        cont += 1
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números. \n A quantidade de números pares é: {}. \n A quantidade de números ímpares é: {}.'.format(cont, par, impar))
