# Para criar uma lista, usa-se colchetes [], diferente das tuplas, que se utiliza parênteses ()
num = [2,3,4,5,6,7]
num[3] = 9 #Substituindo valores
num.append(8) #Adicionando valores
num.sort() #Ordenando a lista
num.sort(reverse=True) #Ordenando a lista de forma contrária
num.insert(2,8) #Adicionando o número 8 na posição 2
num.pop() #Pop sem valor dentro dos parênteses, apaga o último valor
num.pop(0)
num.remove(6) #Remove o número 5 da lista
print(len(num)) # Tamanho da lista
print(num)
