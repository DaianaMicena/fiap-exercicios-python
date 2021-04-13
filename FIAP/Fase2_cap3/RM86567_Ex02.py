print('=-='*10)
print('    TRANSAÇÕES EFETUADAS')
print('=-='*10)

total = 0
qnt = int(input("Informe a quantidade de transações efetuadas hoje: "))

for n in range (qnt):
    valor = float(input("Informe o valor da transação: "))
    total = total + valor

media = total / qnt

print(f"O valor total gasto foi de R$ {round(total,2)} e a média de gasto foi de R$ {round(media,2)}.")








