# Desafio: Adapte o desafio valoresMoedas.py, criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetário formatado.

import moeda



num = float(input('Digite um valor: R$'))
aumentarPor = int(input('Digite a porcentagem do aumento: '))
diminuirPor = int(input('Digite a porcentagem do desconto: '))

print(f'A metade de {num} é {moeda.moeda(moeda.metade(num))}')
print(f'O dobro de {num} é {moeda.moeda(moeda.dobro(num))}')
print(f'Aumentando {aumentarPor}% de {num} ficamos com o valor de {moeda.moeda(moeda.aumentar(num, aumentarPor))}')
print(f'Diminuindo {diminuirPor}% em {num} ficamos com o valor de {moeda.moeda(moeda.diminuir(num, diminuirPor))}')
