# Desafio: Crie um programa que leia três notas de um aluno e calcule sua média, mostrando uma mensagem de acordo com sua média
    # Abaixo de 5pts: REPROVADO;
    # Entre 5pts e 6.9pts: RECUPERAÇÃO;
    # Acima de 7pts: APROVADO.

nota1 = int(input('Digite sua primeira nota: '))
nota2 = int(input('Digite sua segunda nota: '))
nota3 = int(input('Digite sua terceira nota: '))
media = (nota1 + nota2 + nota3) / 3

if media < 5:
    print('Sua média foi de {:.2f}, e você está reprovado!'.format(media))
elif 5 <= media < 7:
    print('Sua média foi de {:.2f}, e você está de recuperação!'.format(media))
else:
    print('Sua média foi de {:.2f}, e você está aprovado!'.format(media))
