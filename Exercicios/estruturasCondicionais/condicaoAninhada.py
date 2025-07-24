nome = str(input('Digite seu nome: '))

if nome == 'Lucas':
    print('Temos o mesmo nome...')
elif nome == 'Maria' or nome == 'Bernardo' or nome == 'Lorena': # elif só funciona se ter um if iniciando a estrutura
    print('Um dos meus sobrinhos tem esse nome...')
elif nome in 'Nubia Camila Luisa':
    print('Uma das minhas irmãs tem ese nome...')
else: # else é opcional
    print('Seu nome é bem normal!')

print('Tenha um bom dia, {}!'.format(nome))
