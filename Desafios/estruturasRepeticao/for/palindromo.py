# Desafio: Crie um programa que crie uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços

frase = str(input('Digite uma palavra ou frase: ')).strip().upper()
palavras = frase.split()
juntando = ''.join(palavras)
inverso = '' # também é possível utilizar o comando inverso = juntando[::-1] para inverter a string, não precisando do for

for letra in range(len(juntando) - 1, -1, -1):
    inverso += juntando[letra]

if inverso == juntando:
    print('"{}" um palíndromo!'.format(frase))
else:
    print('"{}" não é um palíndromo!'.format(frase))
