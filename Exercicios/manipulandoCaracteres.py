texto = 'Curso de python'

# Fatiamento
print(texto[0:5])        # Curso
print(texto[-6:])        # python

# Caixas
print(texto.upper())     # CURSO DE PYTHON
print(texto.lower())     # curso de python
print(texto.title())     # Curso De Python
print(texto.capitalize())# Curso de python

# Substituição
print(texto.replace('Curso de python', 'Estudando Python'))  # Estudando Python

# Divisão
palavras = texto.split()
print(palavras)          # ['Curso', 'de', 'python']
print(palavras[2])       # python

# Verificações
print('python' in texto)         # True
print(texto.startswith('Curso')) # True
print(texto.endswith('python'))  # True

# Junção
print(' '.join(['Estudando', 'Python']))  # Estudando Python

# Remoção de espaços
texto2 = '  Curso de python  '
print(texto2.strip())     # Curso de python

# Tamanho da string
print(len(texto))         # 15

# Índice de substring
print(texto.find('python'))  # 9

# Inverter a string
print(texto[::-1])  # nohtyp ed osruC

# Contar ocorrências de uma substring
print(texto.count('o'))  # 2

# Substituir apenas uma parte (ex: só 'python')
print(texto.replace('python', 'Java'))  # Curso de Java

# Alinhar texto
print(texto.center(30, '-'))  # -------Curso de python--------
print(texto.ljust(20, '*'))   # Curso de python*****
print(texto.rjust(20, '*'))   # *****Curso de python

# Remover uma palavra específica (ex: 'de')
print(' '.join([palavra for palavra in texto.split() if palavra != 'de']))  # Curso python

# Verificar se é alfanumérico
print(texto.isalnum())  # False (por causa dos espaços)

# Converter em lista de caracteres
print(list(texto))  # ['C', 'u', 'r', 's', 'o', ' ', 'd', 'e', ' ', 'p', 'y', 't', 'h', 'o', 'n']

# Usar f-string para montar nova frase com a base da antiga
linguagem = 'Python'
print(f'Estudando {linguagem} com o texto: "{texto}"')

# Transformar em snake_case (substituindo espaços por "_")
print(texto.lower().replace(' ', '_'))  # curso_de_python
