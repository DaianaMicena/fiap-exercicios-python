soma = 0
cont = 0

for n in range (1,7):
    numero = int(input(f'Informe o {n} numero: '))
    if numero % 2 == 0:
        soma += numero
        cont += 1
print(f'Voce informou {cont} numeros pares e a soma total de numeros pares foi {soma}.')
