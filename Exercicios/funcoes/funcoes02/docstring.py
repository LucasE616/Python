# Para fazer uma docstring, basta digitar três aspas duplas na linha abaixo da declaração função

def contador(i, f, p):
    """
    -> Faz uma contagem e mostra o valor da contagem na tela.
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('FIM')


help(contador)
contador(1, 7, 1)
