# Desafio: Escreva um programa que leia um número inteiro e peça para o usuário escolher sua base de conversão:
    # 1 para BINÁRIO
    # 2 para OCTAL
    # 3 para HEXADECIMAL

numero = int(input('Digite um número para converter ele: '))
converter = int(input('Escolha a opção que deseja converter: \n 1 - Binário \n 2 - Octal \n 3 - Hexadecimal \n \n Digite aqui sua escolha: '))
binario = bin(numero)[2:]
octal = oct(numero)[2:]
hexadecimal = hex(numero)[2:].upper()

if converter == 1:
    print('O resultado da conversão do número {} para Binário é: {}'.format(numero, binario))
elif converter == 2:
    print('O resultado da conversão do número {} para Octal é: {}'.format(numero, octal))
elif converter == 3:
    print('O resultado da conversão do número {} para Hexadecimal é: {}'.format(numero, hexadecimal))
else:
    print('Opção inválida. Tente novamente!.')
