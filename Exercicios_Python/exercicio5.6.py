#entrada
peso = float(input("Informe quantos kgs tem o peixe"))
#processamento
limite = 50
if peso > limite:
    excesso = peso - 50
    total = limite + excesso
    multa = excesso * 4
    print(f"Peso limite {limite}kg. \nPeso excedido {excesso}kg. \nPeso total {total}kg. \nO valor a pagar é R$ {round(multa,2)}")
else:
    print(f"Nao ha valor a pagar")