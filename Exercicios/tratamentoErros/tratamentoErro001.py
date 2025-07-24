try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    c = a / b
except (ValueError, TypeError):
    print(f'Tivemos um problema com os tipos de dados...')
except ZeroDivisionError:
    print(f'Não é possível dividir por zero...')
except KeyboardInterrupt:
    print(f'O usuário não informou os dados...')
except Exception as erro:
    print(f'O erro encontrado foi: \n {erro.__cause__}')
else: # Opcional em tratamento de erros com try/except
    print(f'O resultado é {c}')
finally: # Opcional em tratamento de erros com try/except
    print('Volte sempre!')

