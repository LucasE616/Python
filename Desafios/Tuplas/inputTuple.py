# Desafio: Desenvolva um programa que leia 4 valores e guarde-os em uma tupla, no final mostre:
    # Quantas vezes apareceu o valor 9;
    # Em que posição apareceu o valor 3;
    # Quais foram os números pares.

valores = tuple(int(input(f"Digite o {i+1}º valor: ")) for i in range(4)) # também posso utilizar 4 inputs, separados por vírgulas
pares = []
print("Valores digitados:", valores)
print(f'O número 9 apareceu {valores.count(9)} vezes.')

if 3 in valores:
    print(f'O número 3 está na {valores.index(3)+1}º posição')
else:
    print(f'O número 3 não foi digitado')

for c in valores:
    if c % 2 == 0:
        pares.append(c)
if len(pares) == 0:
    print(f'Não existe números pares na lista')
else:
    print(f'Os números pares da lista são: {pares}')

print("Fim do programa!")
