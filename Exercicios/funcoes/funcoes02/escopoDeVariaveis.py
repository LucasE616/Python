def teste():
    x = 9 # x tem o escopo local, ele não irá funcionar fora da função teste()
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')


# Programa principal
n = 3 # n é uma variável de escopo global
print(f'No programa principal, n vale {n}')

teste()
# print(f'No programa principal, x vale {x}') -> O x não funciona aqui, pois tem o escopo local

def segundoTeste(b):
    a = 8 # essa variável é local, permitindo ter duas variáveis A no programa, só que em escopos diferentes
    b += 4
    c = 2
    print(f'A dentro da função vale {a}')
    print(f'B dentro da função vale {b}')
    print(f'C dentro da função vale {c}')


a = 5
segundoTeste(a)
print(f'A fora vale {a}')

def terceiroTeste(nb):
    global na # usando a função global na, conseguimos atualizar a variável global dentro da função, fazendo com que não exista variável NA local
    na = 8
    nb += 4
    nc = 2
    print(f'A dentro da função vale {na}')
    print(f'B dentro da função vale {nb}')
    print(f'C dentro da função vale {nc}')


na = 5
terceiroTeste(na)
print(f'A fora vale {na}')
