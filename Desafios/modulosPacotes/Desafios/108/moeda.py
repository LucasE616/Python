# Criando funções

def moeda(n = 0):
    """
    -> Função para formatar valores
    :param n: recebe um valor
    :return: retorna o valor formatado na tela
    """
    return f'R${n:.2f}'.replace('.', ',')


def metade(n = 0):
    return n / 2

def dobro(n = 0):
    return n * 2


def aumentar(n1 = 0, n2 = 0):
    porcentagem = (n1 * n2) / 100
    aumentado = n1 + porcentagem
    return aumentado


def diminuir(n1 = 0, n2 = 0):
    porcentagem = (n1 * n2) / 100
    diminuido = n1 - porcentagem
    return diminuido

