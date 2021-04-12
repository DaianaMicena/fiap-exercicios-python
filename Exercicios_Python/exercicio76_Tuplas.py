listagem = ('lapis', 1.90,
            'borracha', 2.00,
            'caneta', 4.90,
            'estojo', 5.80,
            'apontado', 7.90)

print('='*30)
print('LISTA DE COMPRAS')
print('='*30)

for l in range(0,len(listagem)):
    if l % 2 == 0:
        print(f'{listagem[l]:.<20}',end=' ')
    else:
        print(f'R$ {listagem[l]:.>3.2f}')


