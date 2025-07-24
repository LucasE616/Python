# \033[0;33;44m
# \033[ style ; text ; background m

# Códigos:
    # Style:      0(none), 1(bold), 4(underline), 7(negative)
    # Text:       30(white), 31(red), 32(green), 33(yellow), 34(blue), 35(violet), 36(cian), 37(gray)
    # Background: 40(white), 41(red), 42(green), 43(yellow), 44(blue), 45(violet), 46(cian), 47(gray)

nome = input('Qual seu nome? ')

cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoBraco' : '\033[7:30m',
         'verde':'\033[32m', }

print('\033[4;34;47mTestando formatação do terminal')
print('\033[0;31;43mTestando formatação do terminal')
print('\033[7;30;41mTestando formatação do terminal\033[m')
print('\033[1;30;43mTestando formatação do \033[1;34;47m terminal')
print('\033[1;34;44mTestando formatação do terminal')
print('\033[1;34;47mTestando formatação do terminal\033[m')

print('Testando outra formatação do terminal com {}{}{}. Ficou assim!'.format('\033[1;34;47m', nome, '\033[m'))
print('Testando mais uma formatação do terminal com {}{}{}. Ficou assim!'.format(cores['azul'], nome, cores['limpa']))
