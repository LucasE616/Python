# Desafio: Elabora um programa que calcule o valor a ser pago por um produto. Considerando o seu preço normal e a condição de pagamento.
    # A vista no dinheiro/PIX: 10% de desconto;
    # A vista no cartão: 5% de desconto;
    # Até duas vezes no cartão: preço normal;
    # 3 vezes no cartão: 20% de juros.

valorProduto = float(input('Digite o valor do produto: '))
metodoPagamento = int(input('Digite a forma de pagamento de acordo com as opções: \n 1 - À Vista no PIX/Dinheiro \n 2 - À Vista no cartão \n 3 - 2x no Cartão \n 4 - 3x no Cartão \n \n Digite a opção escolhida: '))
aVistaDinheiro = valorProduto - (valorProduto * 0.10)
aVistacartao = valorProduto - (valorProduto * 0.05)
parcelado = valorProduto + (valorProduto * 0.20)

if metodoPagamento == 1:
    print('Você irá pagar R${:.2f}'.format(aVistaDinheiro))
elif metodoPagamento == 2:
    print('Você irá pagar R${:.2f}'.format(aVistacartao))
elif metodoPagamento == 3:
    print('Você irá> pagar R${}'.format(valorProduto))
elif metodoPagamento == 4:
    print('Você irá pagar R${:.2f}'.format(parcelado))
else:
    print('Opção inválida. Tente novamente.')
