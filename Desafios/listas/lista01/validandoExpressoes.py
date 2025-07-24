# Desafio: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expressao = str(input('Digite uma expressão: '))
pilha = []

for simbolo in expressao: # for para varrer a expressão(que é uma string) digitada pelo usuário
    # Verificar se é um parêntese abrindo ou fechando
    if simbolo == '(': # Se for um parêntese abrindo...
        pilha.append('(') # Adicione na pilha
    elif simbolo == ')': # Se for um parêntese fechando...
        if len(pilha) > 0: # Se o tamanho da pilha for maior que zero, ela não está vazia, ou seja, existe um parêntese abrindo
            pilha.pop() # Para cada parêntese fechando, remova o último elemento da pilha(que é um parêntese abrindo)
        else: # Se a pilha estiver vazia...
            pilha.append(')') # Adicione um parêntese fechando na pilha
            break
if len(pilha) == 0:
    print('Sua expressão está válida!') # Pois a lista está vazia, graças ao pilha.pop(). Cada parêntese abrindo é apagado da pilha quando encontra um parêntese fechando na expressão
else:
    print('Sua expressão está errada!') # Pois tem um parêntese fechando na pilha, adicionado quando a expressão é inválida
