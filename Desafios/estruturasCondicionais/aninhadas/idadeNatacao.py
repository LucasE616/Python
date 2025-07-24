# Desafio: Crie um programa que leia o ano de nascimento de um atleta, e mostre sua categoria de acordo com sua idade.
    # Até 9 anos: Mirim;
    # Até 14 anos: Infantil;
    # Até 19 anos: Junior;
    # Até 20 anos: Sênior;
    # Acima de 20 anos: Master.

from datetime import date

nascimento = int(input('Digite o ano de nascimento: '))
idade = date.today().year - nascimento

if idade <= 9:
    print('Você tem {} anos, portanto pertence a categoria Mirim'.format(idade))
elif idade <= 14:
    print('Você tem {} anos, portanto pertence a categoria Infantil'.format(idade))
elif idade <= 19:
    print('Você tem {} anos, portanto pertence a categoria Junior'.format(idade))
elif idade >= 20:
    print('Você tem {} anos, portanto pertence a categoria Master'.format(idade))
else:
    print('Você tem {} anos, portanto pertence a categoria Sênior'.format(idade))