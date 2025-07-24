# Desafio: Modifique as funções que criadas no desafio 107 para que aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108

import moeda


num = float(input('Digite um valor: R$'))
aumentarPor = int(input('Digite a porcentagem do aumento: '))
diminuirPor = int(input('Digite a porcentagem do desconto: '))

print(f'A metade de {moeda.moeda(num)} é {moeda.metade(num, True)}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.dobro(num)}')
print(f'Aumentando {aumentarPor}% de {moeda.moeda(num)} ficamos com o valor de {moeda.aumentar(num, aumentarPor, True)}')
print(f'Diminuindo {diminuirPor}% em {moeda.moeda(num)} ficamos com o valor de {moeda.diminuir(num, diminuirPor)}')
