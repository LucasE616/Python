# Desafio 1: Faça um programa que leia um número iteiro e mostre na tela o seu sucessor e seu antecessor
# Desafio 2: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e sua raiz quadrada
# Desafio 3: Faça um programa que mostre a tabuada desse número
# Desafio 4: Crie um programa que leia quanto dinheiro a pessoa tem e mostre quantos dólares a pessoa pode comprar (cotação do dólar em 12/04/2025 é $1 para  R$5,87)

numero = int(input('Digite um valor: '))

sucessor = numero + 1
antecessor = numero - 1

raizQ = numero ** (1/2)

tabuada1 = numero * 1
tabuada2 = numero * 2
tabuada3 = numero * 3
tabuada4 = numero * 4
tabuada5 = numero * 5
tabuada6 = numero * 6
tabuada7 = numero * 7
tabuada8 = numero * 8
tabuada9 = numero * 9
tabuada10 = numero * 10

dolar = numero / 5.87

print('D1: O número digitado foi {}, seu antecessor é {} e seu sucessor é {}'.format(numero, antecessor, sucessor))
print('D2: O dobro do número {} é {}. \n O triplo de {} é {}. \n Já sua raiz quadrada é {}'.format(numero, tabuada2, numero, tabuada3, raizQ))

print('D3: A tabuada do número {} é: \n x 1: {} \n x 2: {} \n x 3: {} \n x 4: {} \n x 5: {} \n x 6: {} \n x 7: {} \n x 8: {} \n x 9: {} \n x 10: {}'.format(numero, tabuada1, tabuada2, tabuada3, tabuada4, tabuada5, tabuada6, tabuada7, tabuada8, tabuada9, tabuada10))

print('D4: Se você tiver {} reais, você pode ter {:.2f} dólares!'.format(numero, dolar))
