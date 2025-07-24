# Desafio: Crie um programa que leia nome, idade e sexo de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
    # Quantas pessoas foram cadastradas;
    # A média de idade do grupo;
    # Uma lista com todas as mulheres do grupo;
    # Uma lista com todas as pessoas com idade acima da média.

listaPessoas = []
pessoa = {}
listaMulheres = []
acimaMediaIdade = []
totalPessoas = 0
totalIdades = 0
mediaIdade = 0

while True:
    pessoa['nome'] = str(input('Nome da pessoa: '))
    pessoa['idade'] = int(input('Idade: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    totalPessoas += 1
    # para calcular o total da idade, também é possível usar  totalIdades += pessoa["idade"]
    listaPessoas.append(pessoa.copy())

    continua = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while continua not in 'SN':
        continua = str(input('Opção inválida! \n Deseja continuar? [S/N]: ')).strip().upper()[0]
    if continua == 'N':
        break

for c in listaPessoas:
    totalIdades += c["idade"]
    if c["sexo"] == "F":
        listaMulheres.append(c["nome"])
mediaIdade = totalIdades / totalPessoas
for c in listaPessoas:
    if c['idade'] > mediaIdade:
        acimaMediaIdade.append(c['nome'])

print(f'O total de pessoas cadastradas foi {totalPessoas}') # Também posso usar o len(listaPessoas) para dizer quantas pessoas foram cadastradas
print(f'A media de idade do grupo é de {mediaIdade:.2f} anos')
print(f'As mulheres cadastradas foram {listaMulheres}')
print(f'As pessoas com idade acima da média são: {acimaMediaIdade}')
