num = 0
soma = 0
cont = 0

while True:
    num = int(input('Digite um numero:'))
    if num == 999:
        break

    soma = soma + num
    cont = cont + 1

print(f'O valor total das somas é {soma} foi digitada {cont} vezes.')
