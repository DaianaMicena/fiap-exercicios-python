
maior = 0
menor = 0
ordem = 0

for p in range (1,6):
    peso = float(input(f'Qual o peso da {p} pessoa? '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O peso maior é da pessoa com {maior} kg. ')
print(f'O peso menor é da pessoa com {menor} kg. ')

