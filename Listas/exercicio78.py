valores = []

for v in range(0,5):
    valores.append(int(input('Adicione um numero: ')))

for p, n in enumerate(valores):
    if n == max(valores):
        print(f'O maior numero é {n} nas posicoes {p}...',end='')
    elif n == min(valores):
       print(f'O menor numero é {n} nas posicoes {p}...',end='')
