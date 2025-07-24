# Desafio: Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC (IMC = peso / altura²) e mostre seu Status de acordo com a tabela abaixo:
    # Abaixo de 18.5: Abaixo do peso;
    # Entre 18.5 e 25: Peso ideal;
    # De 25 a 30: Sobrepeso;
    # De 30 a 40: Obesidade;
    # Acima de 40: Obesidade mórbida.

peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('Seu IMC é de {:.2f}.Você está abaixo do peso.'.format(imc))
elif 18.5 <= imc <25:
    print('Seu IMC é de {:.2f}.Você está no peso ideal.'.format(imc))
elif 25 <= imc < 30:
    print('Seu IMC é de {:.2f}.Você está com sobrepeso.'.format(imc))
elif 30 <= imc < 40:
    print('Seu IMC é de {:.2f}.Você está com obesidade.'.format(imc))
else:
    print('Seu IMC é de {:.2f}.Você está com obesidade mórbida.'.format(imc))