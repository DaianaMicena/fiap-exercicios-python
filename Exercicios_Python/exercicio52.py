from Exercicios_Python.exercicio55lista import check_peso
'''
num = int(input('Informe um numero: '))
total = 0

for n in range(1, num + 1):
    print(n)
    if num % n == 0:
        total += 1
        print('\033[31m', end=' ')
    else:
        print('\033[30m', end=' ')
print(f"\nO numero {num} nao é primo, ele foi divido {total} vezes.")
'''

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(check_peso(lista))