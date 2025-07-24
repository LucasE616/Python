def par(num = 0):
    if num % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número: '))
print(par(num))
if par(num):
    print('Par')
else:
    print('Impar')