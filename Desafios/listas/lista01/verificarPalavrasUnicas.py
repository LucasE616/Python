# Crie um programa que:
#     Peça ao usuário para digitar uma frase completa.
#     Transforme a frase em uma lista de palavras.
#     Mostre:
#         01 - A lista de todas as palavras digitadas. ok
#         02 - Quais palavras apareceram apenas uma vez. ok
#         03 - Quais palavras se repetiram e quantas vezes. ok
#         04 - O total de palavras digitadas. ok
#         05 - O total de palavras únicas (sem repetição) e repetidas. ok
#     Ignore maiúsculas/minúsculas (ou seja, "Casa" e "casa" contam como a mesma palavra).
#     Ignore pontuação (opcional: , . ! ? etc).
import string

frase = str(input('Digite uma frase: ')).strip(".,!?").lower()
listaPalavras = frase.translate(str.maketrans('', '', string.punctuation)) # ignorando pontuação
palavras = listaPalavras.split() # Listando palavras
repetidas = []
naoRepete = []

for palavra in palavras:
    if palavras.count(palavra) > 1:
        repetidas.append(palavra)
    elif palavras.count(palavra) == 1:
        naoRepete.append(palavra)

print(f'A lista digitada foi: {palavras}. E tem tamanho de: {len(palavras)} palavras')
print(f'A lista de palavras repetidas é: {set(repetidas)}. No total foram {len(repetidas)} palavras')
print(f'A lista de palavras que não se repetem é: {naoRepete}. No total foram {len(naoRepete)} palavras')
print(f'A frase sem pontuação é: {listaPalavras}')
