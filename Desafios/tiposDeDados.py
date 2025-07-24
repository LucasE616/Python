# Aula sobtre tipos primitivos
# Alguns deles são: int (Número inteiro), float (Número real), bool (Booleano), str (String)

# desafio: Mostre todos o tipo do valor digitado e mostre se ele se enquadra em alguns formatos

algo = input('Digite algo: ')

print('O tipo primitivo desse valor é: {}'.format(type(algo)))
print('Só tem espaços? ', algo.isspace())
print('É um número? ', algo.isnumeric())
print('É alfabético? ', algo.isalpha())
print('É alfanumérico? ', algo.isalnum())
print('Está em maiúsculas? ', algo.isupper())
print('Está em minúsculas? ', algo.islower())
print('Está captalizada? ', algo.istitle())
