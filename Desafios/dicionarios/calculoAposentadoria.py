# Desafio: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os(com idade) em um dicionário se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime

calcAposentadoria = {}

calcAposentadoria['nome'] = str(input('Digite seu nome: '))
anoNascimento = int(input('Digite seu ano de nascimento: '))
calcAposentadoria['idade'] = datetime.now().year - anoNascimento
calcAposentadoria['ctps'] = int(input('Número Carteira de Trabalho(Digite 0, caso não tenha): '))

if calcAposentadoria['ctps'] == 0:
    print(f'{calcAposentadoria["nome"]} não tem carteira de trabalho.')
elif calcAposentadoria['ctps'] != 0:
    calcAposentadoria['contratacao'] = int(input('Ano de contratação: '))
    calcAposentadoria['salario'] = float(input('Digite seu salário: R$'))
    if datetime.now().year - calcAposentadoria['contratacao'] >= 35:
        calcAposentadoria['aposentadoria'] = 'Já é permitido se aposentar'
    elif datetime.now().year - calcAposentadoria['contratacao'] < 35:
        calcAposentadoria[
            'aposentadoria'] = f'Ainda faltam {35 - (datetime.now().year - calcAposentadoria["contratacao"])} anos para poder se aposentar'
        calcAposentadoria[
            'idadeAposentadoria'] = f'Irá se aprosentar com {calcAposentadoria["idade"] + (35 - (datetime.now().year - calcAposentadoria["contratacao"]))} anos.'

print(calcAposentadoria)
for c, v in calcAposentadoria.items():
    print(f' --> {c} tem o valor {v}')
