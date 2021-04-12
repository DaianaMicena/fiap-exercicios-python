soma = 0
preco = 0
menor = 0
maior = 0
cont = 0
nome = ' '

print('===================')
print('LOJAS LADY DAY')
print('===================')

while True:
    produto = str(input('Nome do produto:'))
    preco = float(input('Qual preco do produtos:'))
    cont +=1
    soma += preco

    if preco > 1000.00:
        maior += 1

    if cont == 1:
        menor = preco
        nome  = produto
    else:
        if menor > preco:
            menor = preco
            nome = produto

    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Quer continuar? [S/N]?')).upper().strip()[0]

    if escolha == 'N':
        break

print('--------- FIM DO PROGRAMA -----------')
print(f'O total das compras foi R$ {soma}.')
print(f'Temos {maior} produto(s) custando mais de R$ 1.000.00.')
print(f'O produto mais barato foi {nome} que custa R$ {menor}.')





