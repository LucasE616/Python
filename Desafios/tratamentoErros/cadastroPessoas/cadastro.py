# Desafio: Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em arquivos de texto simples.
    # O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.


from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'dadosPessoas.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do programa'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do programa...')
        break
    else:
        print('\033[31mERROR!!! \n Digite uma opção válida.\033[m')
    sleep(1)

