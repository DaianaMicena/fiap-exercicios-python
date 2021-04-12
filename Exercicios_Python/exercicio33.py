a = int(input('Informe um numero: '))
b = int(input('Informe um numero: '))
c = int(input('Informe um numero: '))


menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print(f'O maior numero digitado foi {maior}')
print(f'O menor numero digitado foi {menor}')
