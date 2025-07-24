# Desafio: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
    # Quantidade de notas;
    # A maior nota;
    # A menor nota;
    # A média da turma;
    # A situação (opcional).
# Adicione também, as docstrings da função.


def notas(*notasAluno, situacao=False):
    """
    -> Essa função recebe, analisa as notas de um aluno e adiciona esses parâmetros em um dicionário.
    :param notasAluno: Recebe uma ou mais notas do aluno.
    :param situacao: Situação do aluno, baseada na média das notas do aluno (parâmetro opcional).
    :return: Retorna o dicionário com os parâmetros informados.
    """
    boletim = {}
    boletim['total'] = len(notasAluno)
    boletim['Notas'] = notasAluno
    boletim['maior'] = max(notasAluno)
    boletim['menor'] = min(notasAluno)
    boletim['media'] = sum(notasAluno) / len(notasAluno)

    if situacao:
        if boletim['media'] >= 10:
            boletim['situacao'] = 'Ótima'
        elif 10 > boletim['media'] >= 7:
            boletim['situacao'] = 'Boa'
        elif 5 <= boletim['media'] < 7:
            boletim['situacao'] = 'Razoável'
        elif 2 <= boletim['media'] < 5:
            boletim['situacao'] = 'Ruim'
        else:
            boletim['situacao'] = 'Péssima'

    return boletim

resposta = notas(3, 5, 7, 10, 2, 4, 9, 8, 4, 6, situacao=True)
print(resposta)
help(notas)
