def metade(n = 0):
    return n / 2

def dobro(n = 0):
    return n * 2


def aumentar(n1 = 0, n2 = 0):
    porcentagem = (n1 * n2) / 100
    aumentado = n1 + porcentagem
    return aumentado


def diminuir(n1 = 0, n2 = 0, format=False):
    porcentagem = (n1 * n2) / 100
    diminuido = n1 - porcentagem
    return diminuido
