# função para somar dois parâmetros
def soma(a, b):
    print(f'A = {a} | B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')
    print()


soma(1, 2)
soma(32, 25)
soma(175, 250)

# Também posso deixar explicito qual parâmetro é a & b
soma(a=195, b=1250)
soma(b=1750, a=2500) # deixando os parâmetros explicitos, posso inverter a sequência dos parâmetros, mas é melhor evitar

soma('Lucas', 'Emanuel')
