# Desafio: Crie um programa que tenha uma função chamada vota() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto negado, opcional ou obrigatório nas eleições


def vota(nascimento):
    from datetime import date # importando algo dentro de uma função, ela fica apenas no escopo da função, economizando memória
    ano = date.today().year
    idade = ano - nascimento
    if idade < 16:
        return f'Você tem {idade} anos e ainda não pode votar!'
    elif 16 <= idade < 18 or idade >= 70:
        return f'Você tem {idade} anos e pode votar, mas não é obrigatório.'
    elif 18 <= idade < 70:
        return f'Você tem {idade} anos e seu voto é obrigatório!'
    else:
        return None


teste01 = vota(2015)
teste02 = vota(2008)
teste03 = vota(1990)
teste04 = vota(1945)

print(f'Testando resultados: \n Teste 01: {teste01} \n Teste 02: {teste02} \n Teste 03: {teste03} \n Teste 04: {teste04}')

anoNascimento = int(input('Digite o ano de nascimento: '))
print(vota(anoNascimento))
