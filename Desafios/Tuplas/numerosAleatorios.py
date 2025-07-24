# Desafio: Crie um programa que vai gerar 5 números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem dos números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

numeros = tuple(randint(0, 100) for _ in range(5))
ordem = sorted(numeros)
print("Números gerados:", numeros)
print(f'O menor número da lista é {ordem[0]}')
print(f'O menor número da lista é {min(numeros)}') # Forma mais fácil de mostrar o menor número

print(f'O maior número da lista é {ordem[-1]}')
print(f'O maior número da lista é {max(numeros)}') # Forma mais fácil de mostrar o maior número
