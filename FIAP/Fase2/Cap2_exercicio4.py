
#valor
#quantidade
#categoria

valor_bruto = 100.00 #(input("Informe o valor bruto: R$ "))
viajantes = 2 #int(input("Informe a quantidade de viajantes: "))
categoria = 'economica' #str(input("Informe a categoria: "))

#OK
if categoria == "economica" and viajantes == 2:
    print(f"O valor bruto da viagem é R$ {round(valor_bruto,2)} ")
    print(f"O desconto concedido foi de R$ {valor_bruto*0.03}")
    print(f"O valor a pagar será de R$ {valor_bruto-(valor_bruto*0.03)}")
    print(f"O valor por viajante será de R$ {valor_bruto*0.97 / viajantes}")

#OK
if categoria == 'economica' and viajantes == 3:
    print(f"O valor bruto da viagem é R$ {round(valor_bruto, 2)} ")
    print(f"O desconto concedido foi de R$ {valor_bruto * 0.04}")
    print(f"O valor a pagar será de R$ {valor_bruto - (valor_bruto * 0.04)}")
    print(f"O valor por viajante será de R$ {valor_bruto * 0.96 / viajantes}")

#OK
if categoria == 'economica' and viajantes >= 4:
    print(f"O valor bruto da viagem é R$ {round(valor_bruto, 2)} ")
    print(f"O desconto concedido foi de R$ {valor_bruto * 0.05}")
    print(f"O valor a pagar será de R$ {valor_bruto - (valor_bruto * 0.05)}")
    print(f"O valor por viajante será de R$ {valor_bruto * 0.95 / viajantes}")

#OK
if categoria == 'executiva' and viajantes == 2:
    print(f"O valor bruto da viagem é R$ {round(valor_bruto, 2)} ")
    print(f"O desconto concedido foi de R$ {valor_bruto * 0.05}")
    print(f"O valor a pagar será de R$ {valor_bruto - (valor_bruto * 0.05)}")
    print(f"O valor por viajante será de R$ {valor_bruto * 0.95 / viajantes}")

#OK
if categoria == 'executiva' and viajantes == 3:
    print(f"O valor bruto da viagem é R$ {round(valor_bruto, 2)} ")
    print(f"O desconto concedido foi de R$ {round(valor_bruto * 0.07,2)}")
    print(f"O valor a pagar será de R$ {valor_bruto - (valor_bruto * 0.07)}")
    print(f"O valor por viajante será de R$ {round(valor_bruto * 0.93 / viajantes,2)}")

#OK
if categoria == 'executiva' and viajantes >= 4:
    print(f"O valor bruto da viagem é R$ {round(valor_bruto,2)} ")
    print(f"O desconto concedido foi de R$ {valor_bruto * 0.08}")
    print(f"O valor a pagar será de R$ {valor_bruto - (valor_bruto * 0.08)}")
    print(f"O valor por viajante será de R$ {valor_bruto * 0.92 / viajantes} ")

#OK
if categoria == 'primeiraclasse' and viajantes == 2:
    print(f"O valor bruto da viagem é R$ {valor_bruto}")
    print(f"O desconto concedido foi de R$ {valor_bruto * 0.10}")
    print(f"O valor a pagar será de R$ {valor_bruto - (valor_bruto * 0.10)}")
    print(f"O valor por viajante será de R$ {valor_bruto * 0.90 / viajantes}")

#OK
if categoria == 'primeiraclasse' and viajantes == 3:
    print(f"O valor bruto da viagem é R$ {valor_bruto}")
    print(f"O desconto concedido foi de R$ {valor_bruto * 0.15}")
    print(f"O valor a pagar será de R$ {valor_bruto - (valor_bruto * 0.15)}")
    print(f"O valor por viajante será de R$ {round(valor_bruto * 0.85 / viajantes,2)}")

#OK
if categoria == 'primeiraclasse' and viajantes >=4:
    print(f"O valor bruto da viagem é R$ {valor_bruto}")
    print(f"O desconto concedido foi de R$ {valor_bruto * 0.20}")
    print(f"O valor a pagar será de R$ {valor_bruto - (valor_bruto * 0.20)}")
    print(f"O valor por viajante será de R$ {valor_bruto * 0.80 / viajantes}")









