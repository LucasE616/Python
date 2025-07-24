# Desafio: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.No final, mostre:
    # Quantas pessoas foram cadastradas;
    # Uma listagem das pessoas mais pesadas;
    # Uma listagem das pessoas mais leves.

pessoas = []
dados = []
maior = menor = 0
pesados = []
leves = []

# Capturar os nomes e pesos
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()

    cont = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    while cont not in 'SN':
        cont = str(input('Opção inválida! \n Deseja continuar? [S/N] ')).upper().strip()[0]
    if cont == 'N':
        break

# Verificar qual é o maior e o menor peso
for c in range(0, len(pessoas)):
    if c == 0:
        maior = menor = pessoas[c][1]
    elif pessoas[c][1] > maior:
        maior = pessoas[c][1]
    elif pessoas[c][1] < menor:
        menor = pessoas[c][1]

# Verificar quais usuários tem esse peso
for c in pessoas:
    if c[1] == maior:
        pesados.append(c[0])
    elif c[1] == menor:
        leves.append(c[0])

print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'A(s) pessoa(s) mais pesada(s) é(são): {pesados} e pesa(m) {maior}kg.')
print(f'A(s) pessoa(s) mais leve(s) é(são): {leves} e pesa(m) {menor}kg.')
