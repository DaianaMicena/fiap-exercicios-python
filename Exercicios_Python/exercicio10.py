d = float(input('Quanto dinheiro voce tem? '))
conversao = (d / 3.27) * 1.00
conversao1 = (d/6.27) * 1.00
print(f'Com o valor de R$ {round(d,2)} vocë pode comprar USD {round(conversao,2)} ou EUR {round(conversao1,2)}.')
