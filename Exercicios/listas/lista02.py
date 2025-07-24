pessoas = [['Lucas', 22], ['Manuel', 23], ['Maria', 8]]

print(pessoas)
print(pessoas[0][1])
print(pessoas[1][0])
print(pessoas[2])

print(f'\n {'-_' * 25} \n')

teste = list()
teste.append('Lucas')
teste.append(23)
galera = list()
galera.append(teste[:]) # append(teste[:]) dessa maneira é criado uma cópia do teste, da maneira que ele está naquele momento
print(galera)
teste[0] = 'Emanuel'
teste[1] = 22
galera.append(teste[:])
print(galera)

print(f'\n {'-_' * 25} \n')

galeraII = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Marcia', 45]]
print(galeraII)
print(galeraII[2][1]) # Nesse exemplo que estou utilizando, o primeiro colchete é para selecionar uma lista dentro da lista principal, o segundo é para selecionar um item dentro da "sublista"

for p in galeraII:
    print(f'{p[0]} tem {p[1]} anos de idade.')

print(f'\n {'-_' * 25} \n')

galeraIII = []
dado = []
maior = menor = 0
for c in range(0, 5):
    dado.append(str(input('Digite o seu nome: ')))
    dado.append(int(input('Digite sua idade: ')))
    galeraIII.append(dado[:])
    dado.clear()
print(galeraIII)

for p in galeraIII:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade.')
        maior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        menor += 1
print(f'Temos {maior} maiores e {menor} menores de idade.')

