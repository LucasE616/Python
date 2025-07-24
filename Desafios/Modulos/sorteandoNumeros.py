# Desafio 1: Um professor quer sortear um dos seus alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido
# Desafio 2: Faça um programa que leia a o nome dos alunos e mostre a ordem sorteada

import random

alunos = ['Lucas', 'Neto', 'Luma', 'Ana', 'Raissa', 'Samuel', 'Bruno', 'Mathias']

sorteio = random.choice(alunos) # Sorteando um aluno.
ordenandoAlunos = random.shuffle(alunos) # Sorteando a ordem dos alunos. Esse comando serve apenas para embaralhar a lista, caso queira mostrar a lista, printe lista reordenada, nesse caso a variável ALUNOS

print('O aluno escolhido para apagar o quadro foi {}. \n Já a ordem de apresentação é essa: {}'.format(sorteio, alunos))
