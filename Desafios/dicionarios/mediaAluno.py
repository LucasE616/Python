# Desafio: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

escola = {}
escola['Aluno'] = str(input('Nome do aluno: '))
escola['Media'] = float(input(f'Média de {escola["Aluno"]}: '))
if escola['Media'] > 7:
    escola['Situacao'] = 'APROVADO'
elif 5 <= escola['Media'] <= 7:
    escola['Situacao'] = 'RECUPERAÇÃO'
else:
    escola['Situacao'] = 'REPROVADO'

for a, m in escola.items():
    print(f'{a} é {m}')
