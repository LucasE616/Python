# Desafio: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

boletim = []
add = [] # Verificar se é possível eliminar essa lista
aluno = 'lcs'
notas = []
media = 0

# Cadastrando os alunos e suas notas
while True:
    aluno = str(input('Digite o nome do aluno: '))
    notas.append(float(input('Digite a 1° nota do aluno: ')))
    notas.append(float(input('Digite a 2° nota do aluno: ')))
    media = (notas[0] + notas[1]) / 2
    add.append(aluno)
    add.append(notas[:])
    add.append(media)
    boletim.append(add[:])
    notas.clear()
    add.clear()

    continuar = input('Deseja continuar? [S/N]').upper().strip()[0]
    while continuar not in 'SN':
        continuar = input('Opção inválida! \n Deseja continuar? [S/N]').upper().strip()[0]
    if continuar == 'N':
        break

# Mostrando os boletins com a média de todos os alunos
print('-_' * 25)
for c in range(0, len(boletim)):
    print(f'Aluno N° {c}: {boletim[c][0]} -----> Media: {boletim[c][2]}')
print('-_' * 25)

# Mostrar nota individual
while True:
    mostrar = int(input(f'Digite o número do aluno para mostrar suas notas (999 interrompe): '))
    if mostrar == 999:
        break
    elif mostrar <= len(boletim):
        print(f'Aluno: {boletim[mostrar][0]} \n Notas: {boletim[mostrar][1]} \n Media: {boletim[mostrar][2]}')
    else:
        print(f'Opção inválida!')
