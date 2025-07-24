from Desafios.tratamentoErros.cadastroPessoas.lib.inteiros import leiaInt

def linha(tam = 42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mDigite sua opção: \033[m')
    return opc