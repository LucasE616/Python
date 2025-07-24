def contador(*num):
    for valor in num:
        print(valor, end='; ')
    print()
    tamanho = len(num)
    print(f'Recebi os valores: {num} e o tamanho é de {tamanho} parâmetros')
    print('FIM DA FUNÇÃO')
    print()


# Empacotando vários valores, ele insere os parâmetros em uma TUPLA
contador(1, 2, 3)
contador(4, 'numero', 6, 'teste')
contador(7, 8)
