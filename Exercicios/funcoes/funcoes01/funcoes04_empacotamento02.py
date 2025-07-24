def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'A soma dos valores é {s}')

soma(5, 7)
soma(2, 5, 10)
soma(4, 5, 9, 21)
