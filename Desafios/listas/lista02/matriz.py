# Desafio 01: Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz natela com a formatação correta.
# Desafio 02: Aprimore o desafio acima, mostrando no final:
    # A soma de todos os números pares;
    # A soma de todos os valores da terceira coluna;
    # O maior valor da segunda linha.

matriz = [[], [], []]
somaPares = maior = soma3Coluna = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        # Capturando os números para matriz
        matriz[linha].append(int(input(f'Digite um número para posição [{linha}, {coluna}]: ')))

        # Somando os números pares
        if matriz[linha][coluna] % 2 == 0:
            somaPares += matriz[linha][coluna]

        # Somando números da 3° coluna
        if coluna == 2:
            soma3Coluna += matriz[linha][coluna]

        # Verificar qual o maior valor da 2° linha
        if linha == 1:
            if matriz[linha][coluna] > maior:
                maior = matriz[linha][coluna]


# Para mostrar a matriz, também é possível usar um FOR como o FOR feito acima
print(f'\n {matriz[0]} \n {matriz[1]} \n {matriz[2]} \n')
print(f'A soma dos números pares da Matriz é: {somaPares}')
print(f'A soma dos números da 3° coluna da Matriz é: {soma3Coluna}')
print(f'O maior valor da 2° linha é: {maior}')
