# Desafio: Adicione ao módulo moeda.py criado nos desafios anteriores,uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já foram criadas até aqui

import moeda

num = float(input('Digite um valor: R$'))
aumentarPor = int(input('Digite a porcentagem do aumento: '))
diminuirPor = int(input('Digite a porcentagem do desconto: '))

moeda.resumo(num, aumentarPor, diminuirPor)
