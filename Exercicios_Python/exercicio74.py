from random import randint

sorteio = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))

print(f'Os numeros sorteados foram:')

for n in sorteio:
    print(f'{n} ', end='')


print(f'\nO maior numero sorteado foi {max(sorteio)}' )
print(f'O menor numero sorteado foi {min(sorteio)}')