# Desafio: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ao input() do python, só que fazendo a validação para aceitar apenas um valor numérico.
    # Ex: leiaInt('Digite um n')

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('Error!!! \n Digite um número inteiro válido...')
        if ok:
            break
    return valor


n = leiaInt('Digite um número inteiro: ')
print(f'Número inteiro digitado: {n}')
