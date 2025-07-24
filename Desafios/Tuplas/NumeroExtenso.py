# Desafio: Crie um programa que tenha uma tupla preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado e mostrá-lo por extenso.

numExtenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    numEscolhido = int(input('Digite um número entre 0 e 20: '))
    if 0 <= numEscolhido <= 20:
        break
    print('Tente novamente...')
print(f'Aqui está o número {numEscolhido} escrito por extenso: {numExtenso[numEscolhido]}')
