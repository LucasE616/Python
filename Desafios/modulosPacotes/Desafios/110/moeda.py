# Criando funções

def moeda(n = 0):
    """
    -> Função para formatar valores
    :param n: recebe um valor
    :return: retorna o valor formatado na tela
    """
    return f'R${n:.2f}'.replace('.', ',')


def metade(n = 0, format=False):
    """
    -> Função para dividir o valor pela metade
    :param n: recebe o valor a ser dividido
    :param format: parâmetro para verificar se o valor será formatado na tela (opcional)
    :return: retorna o valor dividido pela metade
    """
    if format:
        numMetade = n / 2
        return moeda(numMetade)
    else:
        return n / 2


def dobro(n = 0, format=False):
    """
    -> Função para dobrar os valores
    :param n: recebe o valor a ser dobrado
    :param format: parâmetro para verificar se o valor será formatado na tela (opcional)
    :return: retorna o valor dobrado
    """
    if format:
        numDobro = n * 2
        return moeda(numDobro)
    else:
        return n * 2


def aumentar(n1 = 0, n2 = 0, format=False):
    """
    -> Função para aumentar o valor em determinada porcentagem
    :param n1: recebe o valor a ser aumentado
    :param n2: recebe o valor em % para ser acrescido ao primeiro parâmetro
    :param format: parâmetro para verificar se o valor será formatado na tela (opcional)
    :return: retorna o valor aumentado
    """
    porcentagem = (n1 * n2) / 100
    aumentado = n1 + porcentagem
    if format:
        return moeda(aumentado)
    else:
        return aumentado


def diminuir(n1 = 0, n2 = 0, format=False):
    """
    -> Função para diminuir o valor em determinada porcentagem
    :param n1: recebe o valor a ser diminuido
    :param n2: recebe o valor em % para ser subtraído ao primeiro parâmetro
    :param format: parâmetro para verificar se o valor será formatado na tela (opcional)
    :return: retorna o valor diminuido
    """
    porcentagem = (n1 * n2) / 100
    diminuido = n1 - porcentagem
    if format:
        return moeda(diminuido)
    else:
        return diminuido


def ajuda(x):
    return help(x)


def resumo(x, y, z):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Valor analisado: \t{moeda(x)}')
    print(f'Dobro do valor: \t{dobro(x, True)}')
    print(f'Metade do valor: \t{metade(x, True)}')
    print(f'{y}% de aumento: \t{aumentar(x, y, True)}')
    print(f'{z}% de desconto: \t{diminuir(x, z, True)}')
    print('-' * 30)

