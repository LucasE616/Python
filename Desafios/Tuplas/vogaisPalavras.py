# Desafio: Crie um programa que tenha uma tupla com várias palavras(sem acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('cachorro', 'banana', 'mesa', 'janela', 'computador', 'livro', 'telefone', 'carro', 'papel', 'caneta')

for p in palavras:
    print(f'\n Na palavra {p.upper()} temos: ', end='')
    for letras in p: # cada palavra é uma lista
        if letras in 'aeiou':
            print(f'{letras}', end=' ')
