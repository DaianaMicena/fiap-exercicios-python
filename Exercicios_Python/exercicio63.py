print('SEQUENCIA DE FIBONATTI')

c = 3

n1 = 0
n2 = 1


termos = int(input("Quantos termos voce quer usar? "))

print(f'{n1} -> {n2} ->', end='')

while c <= termos:
    c += 1
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(f' {n3} -> ', end= '')
print(' Fim!')



