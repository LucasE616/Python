# Desafio: Crie um programa onde o usuário possa digitar 5 valores numéricos e cadastre-os em uma lista, já na posição correta de inserção(sem usar o sort()). No Final, mostre a lista ordenada na tela.

lista = []

for c in range(0, 5):
    num = int(input('Digite um valor: '))
    if c == 0 or num > lista[-1]: # Se ele for o primeiro número, ou, se ele for maior que o último valor, acrescente um número ao final
        lista.append(num)
        print(f'Número {num} adicionado ao final da lista... Lista = {lista}')
    else:
        posicao = 0
        while posicao < len(lista): # Enquanto a posição for menor que o tamanho da lista
            if num <= lista[posicao]: # Se o NUM é menor ou igual a LISTA na posição POSICAO
                lista.insert(posicao, num) # Adicione o valor digitado na posição POSICAO
                print(f'Número {num} adicionado na posição {posicao} da lista... Lista = {lista}')
                break
            posicao += 1
print(f'A lista final digitada é: {lista}')
