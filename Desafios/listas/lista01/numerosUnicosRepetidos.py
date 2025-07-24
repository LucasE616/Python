# Desafio: Peça para o usuário digitar 10 números inteiros (um de cada vez ou separados por espaço). Após isso:
    # 1 - Armazene os números em uma lista. ok
    # 2 - Mostre todos os números digitados. ok
    # 3 - Mostre apenas os números únicos (sem repetição). ok
    # 4 - Mostre os números que apareceram mais de uma vez e quantas vezes cada um apareceu. ok
    # 5 - Informe qual foi o maior e menor número digitado. ok
    # 6 - Mostre a lista ordenada de forma decrescente. ok
from itertools import count

entrada = input('Digite 10 números separados por espaço: ')
numeros = list(map(int, entrada.split())) # 1 ok
numUnico = []
numRepetidos = []

for c in range(len(numeros)):
    if numeros.count(numeros[c]) == 1:
        numUnico.append(numeros[c])
    elif numeros.count(numeros[c]) > 1:
        numRepetidos.append(numeros[c])

print(numeros) # 2 ok
print(f'O números únicos são: {set(numUnico)}') # 3 ok
print(f'Os números digitados mais de uma vez são: {set(numRepetidos)}')
for x in range(len(set(numRepetidos))):
    print(f'O número {numRepetidos[x]} foi repetido {numeros.count(numRepetidos[x])} vezes') # 4 ok
print(f'O maior número digitado foi: {max(numeros)}') # 5 ok
print(f'O menor números digitado foi: {min(numeros)}') # 5 ok
print(f'A lista em ordem decrescente é: {sorted(numeros, reverse=True)}') # 6 ok
