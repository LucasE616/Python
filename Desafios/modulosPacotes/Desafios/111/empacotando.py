# Desafio: Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Trasnfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.

from utilidadesCeV import moeda

num = float(input('Digite um valor: R$'))
aumentarPor = int(input('Digite a porcentagem do aumento: '))
diminuirPor = int(input('Digite a porcentagem do desconto: '))

moeda.resumo(num, aumentarPor, diminuirPor)
