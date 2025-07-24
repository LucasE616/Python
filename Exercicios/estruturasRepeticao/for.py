# Somando números:
s = 0
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    s += n
print('A soma dos valores é {}'.format(s))

print('-_-_-_-_-_-')


# 1. Imprimir números de 0 a 4
for i in range(5):
    print(i)

print("-_-_-_-_-_-")


# 2. Percorrer uma lista
frutas = ["maçã", "banana", "laranja"]

for fruta in frutas:
    print(fruta)

print("-_-_-_-_-_-")


# 3. Somar todos os números de uma lista
numeros = [1, 2, 3, 4, 5]
soma = 0

for numero in numeros:
    soma += numero

print("Soma:", soma)

print("-_-_-_-_-_-")


# 4. Usar for com range(start, stop, step)
for i in range(2, 10, 2):
    print(i)

print("-_-_-_-_-_-")


# 5. Repetir uma ação várias vezes
for _ in range(3):
    print("Olá!")
