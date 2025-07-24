def somar(a=0, b=0, c=0): # Também posso usar somar(a=0, b=0, c=0), dessa maneira, todos os valores são opcionais
    """
    -> Soma os três valores e mostra o resultado na tela
    :param a: Primeiro valor (opcional)
    :param b: Segundo valor (opcional)
    :param c: Terceito valor (opcional)
    :return: Resultado da soma
    """
    soma = a + b + c
    return soma

resp1 = somar(5, 4, 3)
resp2 = somar(7, 4, 9)
resp3 = somar(21, 3, 50)
print(f'A primeira soma é {resp1} \n A segunda soma é {resp2} \n A terceito soma é {resp3}')

print(f'A soma é {somar(15, 24, 3)}') # Também é possível usar o print
