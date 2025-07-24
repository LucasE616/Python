# Criando listas
frutas = ["maçã", "banana", "laranja"]
numeros = [1, 2, 3, 4, 5]
mistura = ["texto", 42, True, 3.14]

# Acessando elementos
print("Primeira fruta:", frutas[0])
print("Último número:", numeros[-1])

# Modificando elementos
frutas[1] = "abacaxi"
print("Frutas modificadas:", frutas)

# Adicionando elementos
frutas.append("melancia")
frutas.insert(1, "kiwi")
print("Frutas com novas adições:", frutas)

# Removendo elementos
frutas.remove("maçã")     # Remove "maçã"
removido = frutas.pop()   # Remove o último
print("Frutas após remoções:", frutas)
print("Elemento removido com pop():", removido)

# Tamanho da lista
print("Quantidade de números:", len(numeros))

# Ordenando e invertendo
sorted(numeros)            # Ordena em ordem crescente
print("Números ordenados:", numeros)
numeros.reverse()         # Inverte a ordem
print("Números invertidos:", numeros)

# Loop com listas
print("Frutas disponíveis:")
for fruta in frutas:
    print("-", fruta)

# List comprehension: criando lista de quadrados
quadrados = [x**2 for x in numeros]
print("Quadrados dos números:", quadrados)

# Lista de listas (matriz)
matriz = [
    [1, 2],
    [3, 4],
    [5, 6]
]
print("Elemento da matriz (linha 2, coluna 2):", matriz[1][1])

# Contando e buscando elementos
print("Quantidade de vezes que 2 aparece:", numeros.count(2))
print("Índice do número 3:", numeros.index(3))
