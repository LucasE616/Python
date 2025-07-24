# Tuplas são imutáveis
lanche = ('Hamburger', 'Suco', 'Pizza', 'Pudim', 'Batata frita')
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
d = b + a
pessoa = ('Lucas E.', 23, 'M', 70,5)

for comida in lanche:
    print(f'Estou comendo {comida}')

print("-" * 50)

for cont in range(0, len(lanche)):
    print(f'Vou comer {lanche[cont]} na posição {cont}')

print("-" * 50)

for pos, comida in enumerate(lanche):
    print(f'Estou comendo {comida} na posição {pos}')

print("-" * 50)

print(sorted(lanche)) # ordenando tuplas
print(a)
print(b)
print(c)
print(c.count(5)) # quantas vezes o número 5 aparece
print(c.index(8)) # em que posição está o 8
print(d)
print(d.index(5, 4)) # contando a partir da posição 4, qual a posição do número 5
del(pessoa) # apagando a tupla. A partir disso, pode criar uma nova tupla "pessoa". OBS: não tem como apagar um objeto dentro da tupla

print('Fim')
