# Exemplos de tuplas e usos comuns

# Tupla simples
coordenadas = (10, 20)
print("Coordenadas:", coordenadas)

# Tupla com diferentes tipos de dados
pessoa = ("João", 30, "Engenheiro")
print("Nome:", pessoa[0])
print("Idade:", pessoa[1])

# Desempacotamento de tupla
nome, idade, profissao = pessoa
print(f"{nome} tem {idade} anos e trabalha como {profissao}.")

# Tupla dentro de lista
pontos = [(1, 2), (3, 4), (5, 6)]
for x, y in pontos:
    print(f"Ponto X: {x}, Y: {y}")

# Tupla como chave de dicionário
dados = {("SP", "2023"): 100, ("RJ", "2023"): 80}
print("Dados de SP em 2023:", dados[("SP", "2023")])

# Tupla imutável
configuracoes = ("modo escuro", True, 60)
# configuracoes[0] = "modo claro"  # Isso daria erro, pois tuplas são imutáveis

# Tupla com um único elemento
so_um = (42,)
print("Tupla com um elemento:", so_um)

# Métodos úteis
valores = (1, 2, 2, 3, 4)
print("Quantidade de vezes que 2 aparece:", valores.count(2))
print("Índice do número 3:", valores.index(3))
