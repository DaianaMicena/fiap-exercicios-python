lista = []

while True:

    n = int(input('Digite um numero: '))

    if n not in lista:
        lista.append(n)
        print('Numero adicionado com sucesso!!!')
    else:
        print('Numero duplicado!!!',end= ' ')
        n = int(input('Digite um numero: '))

    r = str(input('Deseja continuar? [S/N]')).upper()

    if r == 'N':
        break

lista.sort()
print(f'Voce digitou os numeros {lista}')

