# Desafio: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
    # Se ele ainda vai se alistar no serviço militar;
        # Caso ainda vai se alistar, diga quanto tempo falta.
    # Se já passou da hora dele se alistar;
        # Se já passou da hora dele se alistar, diga quanto tempo passou.
    # Se é a hora dele se alistar.

from datetime import date

anoNascimento = int(input('Digite o ano do seu nascimento: '))
idade = date.today().year - anoNascimento
menorIdade = 18 - idade
maiorIdade = idade - 18

if idade < 18:
    print('Daqui {} anos, você precisará se alistar no serviço militar! \n Seu alistamento será no ano de {}'.format(menorIdade, date.today().year + menorIdade))
elif idade > 18:
    seAlistou = int(input('Você já se alistou? \n 1 - Sim \n 2 - Não \n \n Digite a opção: '))
    if seAlistou == 1:
        print('Parabéns, você está regularizado.')
    elif seAlistou == 2:
        print('Você precisa se alistar! \n Já está {} anos atrasado!'.format(maiorIdade))
    else:
        print('Opção inválida.')
else:
    print('Você tem {} anos. Está na hora de se alistar!'.format(idade))
