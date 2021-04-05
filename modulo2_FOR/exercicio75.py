
núm = (int(input('Digite um numero: ')), int(input('Digite outro numero: ')),
       int(input('Digite novamente um numero: ')), int(input('Digite o ultimo numero: ')))

print(f'Voce digitou os numeros: {núm}')
print(f'O número 9 apareceu {núm.count(9)} vezes. ')

if 3 in núm:
    print(f'O numero 3 apareceu na {núm.index(3)+1} posicao. ' )
else:
    print('Nao foi digitado o numero 3. ')

for n in núm:
    if n % 2 == 0:
        print(f'{n}', end= ' ')
print(f'Sao numeros pares')


