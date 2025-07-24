# Dicionários

# Para declarar um dicionário, basta colocar chaves na variável
    # EX: dicionário = {}

pessoas = {
    'nome': 'Lucas Emanuel',
    'sexo': 'M',
    'idade': 23,
}

print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.items())

for k in pessoas.values():
    print(k)

del pessoas['sexo']

for k, v in pessoas.items():
    print(f'{k} = {v}')

pessoas['nome'] = 'Emanuel'
pessoas['peso'] = 70
print(pessoas.items())