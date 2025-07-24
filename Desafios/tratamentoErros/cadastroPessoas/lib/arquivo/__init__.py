from Desafios.tratamentoErros.cadastroPessoas.lib.interface import cabecalho
import os

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt') # tentar abrir o arquivo em modo texto (Read Text)
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') # comando para criar um arquivo de texto. OBS: o + serve para criar um arquivo
        a.close()
    except:
        print('\033[31mErro ao criar arquivo\033[m')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('\033[31mErro ao ler arquivo\033[m')
    else:
        if os.path.getsize('dadosPessoas.txt') == 0: # verificar se o arquivo está vazio com base no tamanho do arquivo
            print('Arquivo está vazio.')
        else:
            cabecalho('PESSOAS CADASTRADAS')
            for linha in a:
                dado = linha.split(';')
                dado[1] = dado[1].replace('\n', '')
                print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome = 'Desconhecido', idade = 0):
    try:
        a = open(arq, 'at') # funcionalidade para abrir arquivo e adicionar conteúdo no final desse arquivo
    except:
        print('\033[31mErro ao abrir arquivo...\033[m')
    else:
        try:
            a.write(f'{nome};{idade}\n') # funcionalidade para escrever algo dentro do arquivo
        except:
            print(f'Houve um erro ao adicionar algo no arquivo...\033[m')
        else:
            print(f'Registros de {nome} cadastrado com sucesso!')
            a.close()

