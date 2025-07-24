# Contagem
num = cont = soma = 0
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    soma += num
    cont += 1
print('A soma vale: {}'.format(soma))

# Outra maneira de usar o print, é usando a F String
print(f'Últumo número digitado foi: {num}. Foram digitados {cont} números. E a soma deles é igual a {soma}')
