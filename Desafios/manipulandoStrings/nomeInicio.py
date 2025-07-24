# Desafio: Crie um programa que leia o nome de uma cidade e diga se ele começa com a palavra 'Santo'

cidade = str(input('Digite o nome da cidade: '))
nomeCidade = cidade.strip()
nomeCidade2 = nomeCidade.capitalize()

print(nomeCidade2.startswith('Santo'))