# Mini Projeto: Teste de Exceções em Python

def mostrar_menu():
    print("\n==== MENU DE EXCEÇÕES ====")
    print("1 - SyntaxError")
    print("2 - NameError")
    print("3 - TypeError")
    print("4 - ValueError")
    print("5 - IndexError")
    print("6 - KeyError")
    print("7 - AttributeError")
    print("8 - IndentationError (não pode ser simulado diretamente)")
    print("9 - ZeroDivisionError")
    print("10 - FileNotFoundError")
    print("11 - ImportError")
    print("12 - ModuleNotFoundError")
    print("13 - RuntimeError")
    print("14 - OverflowError")
    print("15 - StopIteration")
    print("16 - MemoryError (evitar rodar!)")
    print("17 - EOFError")
    print("18 - FloatingPointError")
    print("19 - PermissionError")
    print("0 - Sair")

def simular_excecao(opcao):
    if opcao == 1:
        exec("print('Erro de sintaxe')")  # simulado
    elif opcao == 2:
        print(variavel_que_nao_existe)
    elif opcao == 3:
        print("10" + 5)
    elif opcao == 4:
        int("abc")
    elif opcao == 5:
        lista = [1, 2, 3]
        print(lista[10])
    elif opcao == 6:
        dicionario = {"nome": "Joana"}
        print(dicionario["idade"])
    elif opcao == 7:
        numero = 10
        numero.append(5)
    elif opcao == 9:
        print(10 / 0)
    elif opcao == 10:
        open("arquivo_que_nao_existe.txt")
    elif opcao == 11:
        from math import banana
    elif opcao == 12:
        import modulo_inexistente
    elif opcao == 13:
        def recursiva():
            return recursiva()
        recursiva()
    elif opcao == 14:
        print(2.0 ** 10000)
    elif opcao == 15:
        it = iter([1])
        next(it)
        next(it)
    elif opcao == 16:
        lista = [1] * (10 ** 10)
    elif opcao == 17:
        input()  # pode causar EOFError em automação
    elif opcao == 18:
        import numpy as np
        np.seterr(all='raise')
        np.divide(1.0, 0.0)
    elif opcao == 19:
        open("/root/arquivo.txt", "w")

while True:
    mostrar_menu()
    try:
        escolha = int(input("Escolha uma opção: "))
        if escolha == 0:
            print("Encerrando o programa...")
            break
        elif 1 <= escolha <= 19:
            simular_excecao(escolha)
        else:
            print("Opção inválida.")
    except Exception as erro:
        print(f"\n\033[31mExceção capturada: {type(erro).__name__} - {erro}\033[m")
