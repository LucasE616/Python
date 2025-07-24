# Desafio: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

from validandoNumeros import inteiros
from validandoNumeros import floats

inteiro = inteiros.leiaInt('Digite um valor inteiro: ')
real = floats.leiaFloat('Digite um valor real: ')

print(f'\033[0;36mValores digitados:\033[m \n \033[0;34mNúmero inteiro(int): {inteiro} \n Número real(float): {real} \033[m')