# Desafio: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deve perguntar se o usuário quer continuar cadastrando.
    # Ao final mostrar:
        # Quantas pessoas são maiores de idade(18 anos);
        # Quantos homens e mulheres foram cadastrados;
        # Quantas mulheres tem menos de 20 anos.

qHomem = qMulher = cont = mais18 = m20 = 0

while True:
    idade = int(input('Digite sua idade: '))
    if idade >= 18:
        mais18 += 1

    sexo = str(input('Digite seu sexo: [M/F] ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Opção inválida, tente novamente... \n Digite seu sexo: [M/F] '))
    if sexo == 'M':
        qHomem += 1
    elif sexo == 'F':
        qMulher += 1
        if idade < 20:
            m20 += 1

    cont += 1

    continua = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while continua not in 'SN':
        continua = str(input('Opção inválida, tente novamente... \n Deseja continuar? [S/N] ')).strip().upper()[0]
    if continua == 'N':
        break
print(f'Total de pessoas = {cont} \n Quantidade de Homem = {qHomem} \n Quantidade de Mulher = {qMulher} \n Maiores de Idade = {mais18} \n Mulheres com menos de 20 anos = {m20}')
