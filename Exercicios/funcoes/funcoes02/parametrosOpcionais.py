def somar(a, b, c=0): # Fazendo com que c receba 0, a função pode ser chamada somente dois valores.
    """
    -> Soma os três valores e mostra o resultado na tela
    :param a: Primeiro valor (obrigatório)
    :param b: Segundo valor (obrigatório)
    :param c: Terceito valor (opcional)
    """
    soma = a + b + c
    print(f'A soma é {soma}')

def segundaSoma(a=0, b=0, c=0): # Também posso usar somar(a=0, b=0, c=0), dessa maneira, todos os valores são opcionais
    """
    -> Soma os três valores e mostra o resultado na tela
    :param a: Primeiro valor (opcional)
    :param b: Segundo valor (opcional)
    :param c: Terceito valor (opcional)
    """
    soma = a + b + c
    print(f'A segunda soma é {soma}')


somar(7, 4, 3)
somar(4, 5)
print()
segundaSoma(9, 7, 8)
segundaSoma(2, 3)
segundaSoma()
print()

help(somar)
print()
help(segundaSoma)
