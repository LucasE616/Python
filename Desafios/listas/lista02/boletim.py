# Outra solução para o desafio NOTAS

ficha = []

while True:
    nome = str(input('Digite o nome do aluno: '))
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])

    continuar = input('Deseja continuar? [S/N]').upper().strip()[0]
    while continuar not in 'SN':
        continuar = input('Opção inválida! \n Deseja continuar? [S/N]').upper().strip()[0]
    if continuar == 'N':
        break

print('-' * 25)
print(f'{'N°':<4}{'Nome':<10}{'Média':>8}')
print('-' * 25)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:<8.1f}')

while True:
    print('-' * 25)
    opc = int(input('Mostrar notas de qual aluno? (999 para interromper)'))
    if opc == 999:
        break
    elif opc <= len(ficha) - 1:
        print(f'As notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('FIM DO PROGRAMA')