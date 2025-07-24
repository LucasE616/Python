def dobra(lista):
    posicao = 0
    while posicao < len(lista):
        lista[posicao] *= 2
        posicao += 1

valores = [5, 3, 21, 10, 17, 8, 'abc']
print(f'Valores originais: {valores}')
dobra(valores) # Chamando a função, a lista original é alterada
print(valores)
