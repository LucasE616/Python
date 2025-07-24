# Desafio: Crei um programa que leia o nome de uma pessoa e diga:
    # Se ele tem 'Silva' no nome;
    # Qual o primeiro nome da pessoa;
    # Qual o último nome da pessoa.

nome = str(input('Digite seu nome: ')).strip()
dividirNome = nome.split()
primeiroNome = dividirNome[0]
ultimoNome = dividirNome[-1] # outra forma é utilizar a seguinte forma: dividirNome[len(nome)-1]

print('SILVA' in nome.upper())
print(primeiroNome)
print(ultimoNome)
