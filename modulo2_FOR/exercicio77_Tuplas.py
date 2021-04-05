palavras = ('amor','brigadeiro','casa','dedo','escola','fuba','girafa')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos as vogais ',end='')
    for letra in p:
        if letra in 'aeiou':
            print(f'{letra}',end=' ')


