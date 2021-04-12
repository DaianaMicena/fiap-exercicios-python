lista = []

for l in range (0,5):

    n = int(input('Digite um numero: '))
    lista.append(n)

    for p, e in enumerate(lista):
        if n < e:
            lista.insert(p,n)
            break

print(f'{lista}')