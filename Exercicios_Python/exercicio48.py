# variaveis
soma = 0
cont = 0
pares = 0

for c in range(1, 500, 2):
    if c % 3 == 0:
         cont = cont + 1
         soma = soma + c
    print(c)
print(f'O total é {soma}')




