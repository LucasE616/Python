# Desafio: Dentro do pacote utilidadeCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(), mas com uma validação de daods para aceitar apenas valores que sejam monetários.

from utilidadesCeV import moeda
from utilidadesCeV import dado

num = dado.leiaDinheiro('Digite um valor: R$')

aumentarPor = int(input('Digite a porcentagem do aumento: '))
diminuirPor = int(input('Digite a porcentagem do desconto: '))

moeda.resumo(num, aumentarPor, diminuirPor)
