# Desafio 1: Crie um módulo chamado moeda.py que tenha as funções incorporadas:
                                                                            # aumentar()
                                                                            # diminuir()
                                                                            # dobro()
                                                                            # metade()
    # Faça também um programa que importe esse módulo e use algumas dessas funções.

import moeda

num = float(input('Digite um valor: R$'))
aumentarPor = int(input('Digite a porcentagem do aumento: '))
diminuirPor = int(input('Digite a porcentagem do desconto: '))

print(f'A metade de {num} é {moeda.metade(num)}')
print(f'O dobro de {num} é {moeda.dobro(num)}')
print(f'Aumentando {aumentarPor}% de {num} ficamos com o valor de {moeda.aumentar(num, aumentarPor)}')
print(f'Diminuindo {diminuirPor}% em {num} ficamos com o valor de {moeda.diminuir(num, diminuirPor)}')
