def leiaInt(msg):
    while True:
        try:
            n = str(input(msg))
            valor = int(n)
            return valor # return também tem a capacidade de parar o while, como o braak
        except (ValueError, TypeError):
            print(f'\033[0;31mO valor "{n}" é inválido!"\033[m')
        except KeyboardInterrupt:
            print(f'\033[0;31mO usuário encerrou o programa!\033[m')
            return 0

